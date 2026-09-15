# Weighted Pile Merge Cost (Hard)
# Repeatedly merge the two smallest piles until one remains; each merge also
# costs a fixed handling fee. Return the total cost.
# Time: O(n log n) | Space: O(n)

import heapq

def min_merge_cost(weights, fee=0):
    if len(weights) <= 1:
        return 0
    heap = list(weights)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total += merged + fee
        heapq.heappush(heap, merged)
    return total

# Tests
assert min_merge_cost([4, 3, 2, 6]) == 29
assert min_merge_cost([4, 3, 2, 6], fee=1) == 32
assert min_merge_cost([5]) == 0
assert min_merge_cost([]) == 0
print("All tests passed!")
