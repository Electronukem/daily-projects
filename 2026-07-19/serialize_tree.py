# LeetCode 297 - Serialize and Deserialize Binary Tree (Hard)
# Design an algorithm to serialize/deserialize a binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Codec:
    def serialize(self, root):
        tokens = []
        def dfs(node):
            if not node:
                tokens.append("N")
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data):
        it = iter(data.split(","))
        def dfs():
            val = next(it)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Tests
codec = Codec()
#     1
#    / \
#   2   3
#      / \
#     4   5
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
s = codec.serialize(root)
r = codec.deserialize(s)
assert r.val == 1 and r.left.val == 2 and r.right.val == 3
assert r.right.left.val == 4 and r.right.right.val == 5
assert codec.serialize(None) == "N"
assert codec.deserialize("N") is None
print(f"Serialized: {s}")
print("All tests passed!")
