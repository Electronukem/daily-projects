# LeetCode 51 - N-Queens (Hard)
# Place N queens on an NxN board so no two attack each other.
# Time: O(N!) | Space: O(N)

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, diag, anti = set(), set(), set()

        def backtrack(row, board):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti:
                    continue
                cols.add(col); diag.add(row - col); anti.add(row + col)
                board[row][col] = 'Q'
                backtrack(row + 1, board)
                board[row][col] = '.'
                cols.remove(col); diag.remove(row - col); anti.remove(row + col)

        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return res

# Tests
sol = Solution()
ans4 = sol.solveNQueens(4)
assert len(ans4) == 2
ans8 = sol.solveNQueens(8)
assert len(ans8) == 92
print(f"4-Queens: {len(ans4)} solutions, 8-Queens: {len(ans8)} solutions")
print("All tests passed!")
