# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # create sorted array of all values
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        vals = dfs(root)
        
        # create new BST
        def createTree(arr):
            if not arr:
                return
            m = len(arr)//2
            return TreeNode(arr[m], createTree(arr[:m]), createTree(arr[m+1:]))
        return createTree(vals)
