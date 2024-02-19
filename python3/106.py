# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(inorder):
            curr = postorder.pop()
            node = TreeNode(curr)
            left, right = inorder[:inorder.index(curr)], inorder[inorder.index(curr) + 1:]
            node.right = build(right) if right else None
            node.left = build(left) if left else None
            return node

        return build(inorder)
