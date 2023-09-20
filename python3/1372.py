# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(count, node, prev):
            if not node:
                return count
            count += 1
            if prev == "left":
                count = max(dfs(0, node.left, "left"), dfs(count, node.right, "right"))
            else:
                count = max(dfs(count, node.left, "left"), dfs(0, node.right, "right"))
            return count

        return max(dfs(0, root.left, "left"), dfs(0, root.right, "right"))
