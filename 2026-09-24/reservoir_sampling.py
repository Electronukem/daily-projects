# Reservoir Sampling (Hard)
# Select a uniform random sample of size k from a stream of unknown length
# in a single pass and O(k) space (Algorithm R).
# Time: O(n) | Space: O(k)

import random

def reservoir_sample(stream, k, seed=None):
    rng = random.Random(seed)
    sample = []
    for i, item in enumerate(stream):
        if i < k:
            sample.append(item)
        else:
            j = rng.randint(0, i)
            if j < k:
                sample[j] = item
    return sample

# Tests
result1 = reservoir_sample(range(100), 5, seed=123)
result2 = reservoir_sample(range(100), 5, seed=123)
assert result1 == result2                     # deterministic given a seed
assert len(result1) == 5
assert len(set(result1)) == 5
assert all(0 <= x < 100 for x in result1)
assert reservoir_sample([1, 2, 3], 5) == [1, 2, 3]  # k > stream length
print("All tests passed!")
