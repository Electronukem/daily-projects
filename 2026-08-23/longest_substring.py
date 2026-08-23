# LeetCode 3 - Longest Substring Without Repeating Characters (Medium)
# Given a string s, find the length of the longest substring without repeating chars.
# Time: O(n) | Space: O(min(n, alphabet))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = res = 0
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            seen[ch] = right
            res = max(res, right - left + 1)
        return res

# Tests
sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
assert sol.lengthOfLongestSubstring("") == 0
assert sol.lengthOfLongestSubstring("dvdf") == 3
print("All tests passed!")
