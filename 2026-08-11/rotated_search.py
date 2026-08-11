# LeetCode 33 - Search in Rotated Sorted Array (Medium)
# Search target in a rotated sorted array in O(log n).

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

# Tests
sol = Solution()
assert sol.search([4,5,6,7,0,1,2], 0) == 4
assert sol.search([4,5,6,7,0,1,2], 3) == -1
assert sol.search([1], 0) == -1
assert sol.search([3,1], 1) == 1
print("All tests passed!")
