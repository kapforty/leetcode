# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        candidates = set()
        def dfs(node, currString):
            nonlocal candidates
            currString = chr(ord('a') + node.val) + currString
            if not node.left and not node.right:
                candidates.add(currString)
                return
            if node.left:
                dfs(node.left, currString)
            if node.right:
                dfs(node.right, currString)
        dfs(root, "")
        candidates = sorted(list(candidates))
        return candidates[0]
