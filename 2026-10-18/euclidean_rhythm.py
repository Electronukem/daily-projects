# Euclidean Rhythm Generator (Medium)
# Distribute k pulses as evenly as possible across n steps — the algorithm
# behind many world-music rhythms and drum-machine patterns.
# Time: O(steps) | Space: O(steps)

def euclidean_rhythm(pulses, steps):
    if pulses <= 0:
        return [0] * steps
    if pulses >= steps:
        return [1] * steps
    pattern, prev = [], -1
    for i in range(steps):
        cur = (i * pulses) // steps
        pattern.append(1 if cur != prev else 0)
        prev = cur
    return pattern

# Tests
assert euclidean_rhythm(3, 8) == [1, 0, 0, 1, 0, 0, 1, 0]  # the classic "tresillo"
assert euclidean_rhythm(0, 4) == [0, 0, 0, 0]
assert euclidean_rhythm(4, 4) == [1, 1, 1, 1]
assert sum(euclidean_rhythm(5, 8)) == 5
assert len(euclidean_rhythm(5, 8)) == 8
print("All tests passed!")
