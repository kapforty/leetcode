# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         return self.count(root, k, 0).val
    
#     def count(self, node, k, count):
#         if not node:
#             return count

#         if node.left:
#             left = self.count(node.left, k, count)
#             if not isinstance(left, int):
#                 return left
#             count = left

#         count += 1
#         if count == k:
#             return node

#         if node.right:
#             right = self.count(node.right, k, count)
#             if not isinstance(right, int):
#                 return right
#             count = right

#         return count