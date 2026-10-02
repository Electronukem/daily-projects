# Open-Addressing Hash Table (Hard)
# A hash table using linear probing with tombstone deletion, so lookups for
# keys past a deleted slot still probe correctly.
# Time: O(1) average per operation | Space: O(capacity)

class HashTable:
    _DELETED = object()

    def __init__(self, capacity=16):
        self.capacity = capacity
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.count = 0

    def _hash(self, key):
        h = 0
        for ch in str(key):
            h = (h * 31 + ord(ch)) % self.capacity
        return h

    def _probe(self, key):
        idx = self._hash(key)
        first_free = None
        for _ in range(self.capacity):
            slot = self.keys[idx]
            if slot is None:
                return (first_free if first_free is not None else idx), False
            if slot is self._DELETED:
                if first_free is None:
                    first_free = idx
            elif slot == key:
                return idx, True
            idx = (idx + 1) % self.capacity
        return (first_free if first_free is not None else None), False

    def put(self, key, value):
        if self.count >= self.capacity * 0.7:
            self._resize()
        idx, found = self._probe(key)
        if idx is None:
            raise RuntimeError("hash table full")
        if not found:
            self.count += 1
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx, found = self._probe(key)
        if not found:
            raise KeyError(key)
        return self.values[idx]

    def delete(self, key):
        idx, found = self._probe(key)
        if not found:
            raise KeyError(key)
        self.keys[idx] = self._DELETED
        self.values[idx] = None
        self.count -= 1

    def __contains__(self, key):
        return self._probe(key)[1]

    def _resize(self):
        old_keys, old_values = self.keys, self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.count = 0
        for k, v in zip(old_keys, old_values):
            if k is not None and k is not self._DELETED:
                self.put(k, v)

# Tests
ht = HashTable(capacity=8)
ht.put("a", 1); ht.put("b", 2); ht.put("c", 3)
assert ht.get("a") == 1
assert "b" in ht and "z" not in ht

ht.delete("b")
assert "b" not in ht
try:
    ht.get("b")
    assert False, "should have raised"
except KeyError:
    pass

ht.put("b", 20)  # reuse the tombstoned slot
assert ht.get("b") == 20 and ht.count == 3

for i in range(20):
    ht.put(f"key{i}", i)
assert all(ht.get(f"key{i}") == i for i in range(20))
assert ht.get("a") == 1  # survives resize
print("All tests passed!")
