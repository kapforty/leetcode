# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = []

        # first bfs
        currLevel = [root]
        while currLevel:
            levelSum = 0
            nextLevel = []
            for node in currLevel:
                levelSum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            levels.append(levelSum)
            currLevel = nextLevel

        # second bfs
        currLevel, i = [root], 0
        while currLevel:
            nextLevel = []
            for node in currLevel:
                node.val = levels[i] - node.val
                if node.left and node.right:
                    node.left.val = node.right.val = node.left.val + node.right.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel
            i += 1
        return root
