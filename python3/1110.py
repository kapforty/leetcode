# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        candidates = [root] if root.val not in to_delete else []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left and node.left.val in to_delete:
                node.left = None
            if node.right and node.right.val in to_delete:
                node.right = None
            if node.val in to_delete:
                if node.left:
                    candidates.append(node.left)
                if node.right:
                    candidates.append(node.right)
            return

        dfs(root)

        res = []
        for candidate in candidates:
            if candidate.val not in to_delete:
                res.append(candidate)
        return res
