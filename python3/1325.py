# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:    
        def dfs(node):
            if not node:
                return
            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None
            if node.val == target and not node.left and not node.right:
                return True
        dfs(root)

        if root.val == target and not root.left and not root.right:
            return None

        return root
        
