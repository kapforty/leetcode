# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# --- O(N) RUNTIME, O(1) SPACE COMPLEXITY ---
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = prev = float("inf")
             
        def inorder(node):
            nonlocal res, prev
            if not node:
                return
            inorder(node.left)
            if abs(node.val - prev) < res:
                res = abs(node.val - prev)
            prev = node.val
            inorder(node.right)
            
        inorder(root)

        return res

# --- O(N) RUNTIME, O(N) SPACE COMPLEXITY ---
# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         res = float("inf")
#         vals = []

#         def inorder(node):
#             nonlocal vals
#             if not node:
#                 return
#             inorder(node.left)
#             vals.append(node.val)
#             inorder(node.right)

#         inorder(root)

#         for i in range(len(vals) - 1):
#             if vals[i+1] - vals[i] < res:
#                 res = vals[i+1] - vals[i]

#         return res
