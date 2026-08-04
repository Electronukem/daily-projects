# LeetCode 124 - Binary Tree Maximum Path Sum (Hard)
# Find the maximum path sum in a binary tree (any node to any node).
# Time: O(n) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.ans

# Tests
sol = Solution()
t1 = TreeNode(1, TreeNode(2), TreeNode(3))
assert sol.maxPathSum(t1) == 6  # 2 -> 1 -> 3

t2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert sol.maxPathSum(t2) == 42  # 15 -> 20 -> 7

t3 = TreeNode(-3)
assert sol.maxPathSum(t3) == -3
print("All tests passed!")
