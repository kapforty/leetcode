# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, parent=None):
            nonlocal res
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)
            if node.val != 1:
                diff = 1 - node.val
                node.val += diff
                parent.val -= diff
                res += abs(diff)
        dfs(root)
        return res
        
