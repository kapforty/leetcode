# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def diameter(node):
            nonlocal res
            if not node:
                return 0
            left = right = 0
            if node.left:
                left = 1 + diameter(node.left)
            if node.right:
                right = 1 + diameter(node.right)
            res = max(res, left + right)
            return max(left, right)

        diameter(root)

        return res
