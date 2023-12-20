# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, count):
            nonlocal res
            count *= 10
            count += node.val
            if not node.left and not node.right:
                res += count
                return
            if node.left:
                dfs(node.left, count)
            if node.right:
                dfs(node.right, count)
        dfs(root, 0)

        return res
