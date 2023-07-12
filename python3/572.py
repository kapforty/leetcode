# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            if self.check(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def check(self, root, subroot):
        if not root and not subroot:
            return True
        if not root or not subroot or root.val != subroot.val:
            return False
        return self.check(root.left, subroot.left) and self.check(root.right, subroot.right)
