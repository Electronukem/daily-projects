# Elevator Dispatch Order (Hard)
# Given a starting floor and a set of pickup requests, produce the visiting
# order using the SCAN (elevator) algorithm: serve everything in the current
# direction first, then reverse.
# Time: O(n log n) | Space: O(n)

def elevator_order(start_floor, requests):
    up = sorted(set(f for f in requests if f >= start_floor))
    down = sorted(set(f for f in requests if f < start_floor), reverse=True)
    return up + down

# Tests
assert elevator_order(5, [8, 2, 5, 9, 1, 6]) == [5, 6, 8, 9, 2, 1]
assert elevator_order(0, [-3, 1, -1, 2]) == [1, 2, -1, -3]
print("All tests passed!")
