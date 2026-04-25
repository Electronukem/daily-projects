# LeetCode 91 - Decode Ways (Medium)
# Count ways to decode a digit string where 1-26 map to A-Z.
# Time: O(n) | Space: O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        prev2, prev1 = 1, 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr += prev1
            two = int(s[i-1:i+1])
            if 10 <= two <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr
        return prev1

# Tests
sol = Solution()
assert sol.numDecodings("12") == 2    # AB or L
assert sol.numDecodings("226") == 3   # BBF, BZ, VF
assert sol.numDecodings("06") == 0
assert sol.numDecodings("10") == 1
assert sol.numDecodings("2101") == 1
print("All tests passed!")
