# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSums = []
        currLevel = [root]
        while currLevel:
            nextLevel, currSum = [], 0
            for node in currLevel:
                currSum += node.val
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel
            levelSums.append(currSum)
        levelSums.sort(reverse=True)
        return -1 if k > len(levelSums) else levelSums[k-1]
