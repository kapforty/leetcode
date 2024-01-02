# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            res = max(res, node.val, left + right + node.val, left + node.val, right + node.val)
            return max(node.val, left + node.val, right + node.val)
            
        dfs(root)
        
        return res
