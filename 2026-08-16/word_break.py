# LeetCode 139 - Word Break (Medium)
# Given a string s and a dictionary, return true if s can be segmented into words.
# Time: O(n^2) | Space: O(n)

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[len(s)]

# Tests
sol = Solution()
assert sol.wordBreak("leetcode", ["leet", "code"]) == True
assert sol.wordBreak("applepenapple", ["apple", "pen"]) == True
assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
print("All tests passed!")
