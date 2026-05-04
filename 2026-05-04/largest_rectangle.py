# LeetCode 84 - Largest Rectangle in Histogram (Hard)
# Find the area of the largest rectangle in a histogram.
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

# Tests
sol = Solution()
assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10
assert sol.largestRectangleArea([2,4]) == 4
assert sol.largestRectangleArea([1]) == 1
assert sol.largestRectangleArea([0]) == 0
print("All tests passed!")
