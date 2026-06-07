# LeetCode 4 - Median of Two Sorted Arrays (Hard)
# Find the median of two sorted arrays in O(log(min(m,n))).

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = (m + n + 1) // 2 - i
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1

# Tests
sol = Solution()
assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert sol.findMedianSortedArrays([], [1]) == 1.0
print("All tests passed!")
