# Grid Treasure Path (Hard)
# Walk from the top-left to the bottom-right of a grid (right/down moves only)
# collecting the maximum treasure, where -1 marks a blocked cell.
# Returns -1 if no path exists.
# Time: O(rows * cols) | Space: O(rows * cols)

def max_treasure(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == -1 or grid[rows - 1][cols - 1] == -1:
        return -1
    dp = [[-1] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == -1:
                dp[r][c] = -1
                continue
            if r == 0 and c == 0:
                continue
            best = -1
            if r > 0 and dp[r - 1][c] != -1:
                best = max(best, dp[r - 1][c])
            if c > 0 and dp[r][c - 1] != -1:
                best = max(best, dp[r][c - 1])
            dp[r][c] = best + grid[r][c] if best != -1 else -1
    return dp[rows - 1][cols - 1]

# Tests
assert max_treasure([[1, 3, 1], [1, -1, 1], [4, 2, 1]]) == 9
assert max_treasure([[-1, 2], [3, 4]]) == -1
assert max_treasure([[0, -1], [-1, 0]]) == -1
print("All tests passed!")
