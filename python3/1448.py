# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(maxVal, node):
            if not node:
                return
            if node.val >= maxVal:
                self.res += 1
            maxVal = max(maxVal, node.val)
            dfs(maxVal, node.left)
            dfs(maxVal, node.right)
        dfs(-inf, root)
        return self.res
