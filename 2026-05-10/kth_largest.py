# LeetCode 215 - Kth Largest Element in an Array (Medium)
# Find the kth largest element using Quickselect.
# Time: O(n) average | Space: O(1)

from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # convert to kth smallest

        def quickselect(lo, hi):
            pivot_idx = random.randint(lo, hi)
            nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
            pivot = nums[hi]
            store = lo
            for i in range(lo, hi):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[hi] = nums[hi], nums[store]
            if store == k:
                return nums[store]
            elif store < k:
                return quickselect(store + 1, hi)
            else:
                return quickselect(lo, store - 1)

        return quickselect(0, len(nums) - 1)

# Tests
sol = Solution()
assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5
assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
print("All tests passed!")
