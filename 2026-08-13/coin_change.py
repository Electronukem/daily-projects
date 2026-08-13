# LeetCode 322 - Coin Change (Medium)
# Return the fewest number of coins needed to make up the amount.
# Time: O(amount * n) | Space: O(amount)

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# Tests
sol = Solution()
assert sol.coinChange([1, 5, 10, 25], 30) == 2
assert sol.coinChange([2], 3) == -1
assert sol.coinChange([1], 0) == 0
assert sol.coinChange([1, 2, 5], 11) == 3
print("All tests passed!")
