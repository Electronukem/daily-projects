# LeetCode 76 - Minimum Window Substring (Hard)
# Find the smallest window in s that contains all characters of t.
# Time: O(n) | Space: O(k) where k = unique chars in t

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left < end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]

# Tests
sol = Solution()
assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert sol.minWindow("a", "a") == "a"
assert sol.minWindow("a", "aa") == ""
print("All tests passed!")
