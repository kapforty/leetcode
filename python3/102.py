# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        deque = collections.deque()
        if root:
            deque.append(root)

        while deque:
            vals = []
            for _ in range(len(deque)):
                node = deque.popleft()
                vals.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(vals)
        return res

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         stack = [root]
#         while stack:
#             vals, temp = [], []
#             for node in stack:
#                 if not node:
#                     continue
#                 vals.append(node.val)
#                 temp.append(node.left)
#                 temp.append(node.right)
#             res.append(vals)
#             stack = temp
#         res.pop()
#         return res