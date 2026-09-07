# Peak Concurrent Load (Hard)
# Given weighted, half-open time intervals, find the maximum total load
# active at any single instant using a sweep line.
# Time: O(n log n) | Space: O(n)

def max_concurrent_load(intervals):
    events = []
    for s, e, load in intervals:
        events.append((s, 1, load))
        events.append((e, 0, -load))
    events.sort(key=lambda ev: (ev[0], ev[1]))
    current = peak = 0
    for _, _, delta in events:
        current += delta
        peak = max(peak, current)
    return peak

# Tests
assert max_concurrent_load([(0, 10, 5), (5, 15, 3), (10, 20, 2)]) == 8
assert max_concurrent_load([(0, 5, 1), (0, 5, 1), (0, 5, 1)]) == 3
print("All tests passed!")
