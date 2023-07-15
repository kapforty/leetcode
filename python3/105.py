# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # current node
        node = TreeNode(preorder[0], None, None)
        idx = inorder.index(preorder[0])

        # left subtree
        node.left = self.buildTree(preorder[1:idx+1], inorder[:idx])

        # right subtree
        node.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return node


# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None

#         # current node
#         val = preorder[0]
#         node = TreeNode(val, None, None)

#         # left subtree
#         node.left = self.buildTree(preorder[1:], inorder[:inorder.index(val)])

#         # right subtree
#         inorder = inorder[inorder.index(val) + 1:]
#         if not inorder:
#             node.right = None
#         else:
#             while preorder[0] not in inorder:
#                 preorder = preorder[1:]
#             node.right = self.buildTree(preorder, inorder)

#         return nod
