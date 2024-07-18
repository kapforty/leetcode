# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node:
                return []
            left, right = dfs(node.left), dfs(node.right)
            if not node.left and not node.right:
                return [0]
            for i in range(len(left)): left[i] += 1
            for i in range(len(right)): right[i] += 1
            for dist1 in left:
                for dist2 in right:
                    if dist1 + dist2 <= distance:
                        res += 1
            return left + right
        dfs(root)
        
        return res
