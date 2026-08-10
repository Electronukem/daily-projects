# LeetCode 72 - Edit Distance (Hard)
# Find min operations (insert, delete, replace) to convert word1 to word2.
# Time: O(mn) | Space: O(n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))
        for i in range(1, m + 1):
            curr = [i] + [0] * n
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
            prev = curr
        return prev[n]

# Tests
sol = Solution()
assert sol.minDistance("horse", "ros") == 3
assert sol.minDistance("intention", "execution") == 5
assert sol.minDistance("", "abc") == 3
assert sol.minDistance("abc", "abc") == 0
print("All tests passed!")
