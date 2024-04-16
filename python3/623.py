# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # trivial case
        if depth == 1:
            return TreeNode(val, root)

        # use dfs to recurse to correct depth, add row when reached
        def dfs(node, count):
            if not node:
                return
            if count == depth:
                tempL, tempR = node.left, node.right
                node.left = TreeNode(val, tempL, None)
                node.right = TreeNode(val, None, tempR)
                return
            else:
                dfs(node.left, count + 1)
                dfs(node.right, count + 1)
        dfs(root, 2)

        return root
