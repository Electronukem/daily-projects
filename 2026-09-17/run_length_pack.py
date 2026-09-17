# Run-Length Pack (Medium)
# Compress a list of values into (value, count) runs, and unpack it back.
# Time: O(n) | Space: O(n)

def rle_pack(items):
    if not items:
        return []
    packed = []
    cur, count = items[0], 1
    for x in items[1:]:
        if x == cur:
            count += 1
        else:
            packed.append((cur, count))
            cur, count = x, 1
    packed.append((cur, count))
    return packed

def rle_unpack(packed):
    out = []
    for val, count in packed:
        out.extend([val] * count)
    return out

# Tests
assert rle_pack([1, 1, 1, 2, 2, 3]) == [(1, 3), (2, 2), (3, 1)]
assert rle_unpack([(1, 3), (2, 2), (3, 1)]) == [1, 1, 1, 2, 2, 3]
assert rle_pack([]) == []
assert rle_unpack(rle_pack([5, 5, 5, 5])) == [5, 5, 5, 5]
print("All tests passed!")
