# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        # current node
        root, preorder, postorder = TreeNode(preorder[0]), preorder[1:], postorder[:-1]
        if not preorder: return root
        idx = postorder.index(preorder[0])

        # left subtree
        root.left = self.constructFromPrePost(preorder[:idx + 1], postorder[:idx + 1])

        # right subtree
        root.right = self.constructFromPrePost(preorder[idx + 1:], postorder[idx + 1:])
        
        return root
