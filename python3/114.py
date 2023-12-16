# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# --- O(N) RUNTIME, O(1) SPACE COMPLEXITY ---
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        curr = root
        while curr:
            if curr.left:
                rightChild = curr.right
                curr.right = curr.left
                curr.left = None
                if rightChild:
                    temp = curr
                    while temp.right:
                        temp = temp.right
                    temp.right = rightChild
            curr = curr.right
        return root

# --- O(N) RUNTIME, O(N) SPACE COMPLEXITY ---
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        traversal = []

        def preorder(node):
            nonlocal traversal
            if not node:
                return
            traversal.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        root.left = None
        root.right = None
        root.val = traversal[0]
        curr = root

        for val in traversal[1:]:
            curr.right = TreeNode(val)
            curr = curr.right

        return root
