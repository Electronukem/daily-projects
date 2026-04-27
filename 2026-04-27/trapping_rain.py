# LeetCode 42 - Trapping Rain Water (Hard)
# Given n non-negative integers representing an elevation map, compute trapped water.
# Time: O(n) | Space: O(1)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water

# Tests
sol = Solution()
assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
assert sol.trap([4,2,0,3,2,5]) == 9
assert sol.trap([]) == 0
assert sol.trap([3]) == 0
print("All tests passed!")
