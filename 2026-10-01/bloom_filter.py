# Bloom Filter (Medium)
# A probabilistic set with no false negatives and a tunable false-positive
# rate, backed by k independent hash functions over a shared bit array.
# Time: O(k) per operation | Space: O(size)

import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bits = [0] * size

    def _hashes(self, item):
        data = str(item).encode()
        for i in range(self.num_hashes):
            digest = hashlib.sha256(data + str(i).encode()).hexdigest()
            yield int(digest, 16) % self.size

    def add(self, item):
        for idx in self._hashes(item):
            self.bits[idx] = 1

    def might_contain(self, item):
        return all(self.bits[idx] for idx in self._hashes(item))

# Tests
bf = BloomFilter(1000, 4)
present = ["apple", "banana", "cherry", "date"]
for word in present:
    bf.add(word)
assert all(bf.might_contain(word) for word in present)  # never a false negative

absent = ["xylophone", "zeppelin", "quokka"]
assert sum(bf.might_contain(word) for word in absent) == 0
print("All tests passed!")
