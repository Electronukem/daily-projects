# LeetCode 56 - Merge Intervals (Medium)
# Given an array of intervals, merge all overlapping intervals.
# Time: O(n log n) | Space: O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

# Tests
sol = Solution()
assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert sol.merge([[1,4],[4,5]]) == [[1,5]]
assert sol.merge([[1,4],[0,4]]) == [[0,4]]
assert sol.merge([[1,4],[2,3]]) == [[1,4]]
print("All tests passed!")
