# LeetCode 15 - Three Sum (Medium)
# Given an array nums, return all triplets [a,b,c] such that a+b+c=0.
# Time: O(n^2) | Space: O(1) extra (excluding output)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return res

# Tests
sol = Solution()
assert sorted(sol.threeSum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
assert sol.threeSum([0, 1, 1]) == []
assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
print("All tests passed!")
