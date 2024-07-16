# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pathToStart, pathToDest = [], []
        def dfs(node, path):
            nonlocal pathToStart, pathToDest
            if not node:
                return
            if node.val == startValue:
                pathToStart = path.copy()
            if node.val == destValue:
                pathToDest = path.copy()
            path.append("L")
            dfs(node.left, path)
            path.pop()
            path.append("R")
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        
        pathToStart = "".join(pathToStart)
        pathToDest = "".join(pathToDest)

        while pathToStart and pathToDest and pathToStart[0] == pathToDest[0]:
            pathToStart = pathToStart[1:]
            pathToDest = pathToDest[1:]
        pathToStart = "U" * len(pathToStart)

        return pathToStart + pathToDest
