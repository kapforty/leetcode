# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkValid(root, float("-inf"), float("inf"))

    def checkValid(self, node, leftBound, rightBound):
        if node.val <= leftBound or node.val >= rightBound:
            return False

        left = True
        right = True
        if node.left:
            left = self.checkValid(node.left, leftBound, node.val)
        if node.right:
            right = self.checkValid(node.right, node.val, rightBound)

        return left and right