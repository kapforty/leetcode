# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        frontier = [root]

        while frontier:
            currSum = 0
            count = 0
            nextFrontier = []
            for node in frontier:
                currSum += node.val
                count += 1
                if node.left:
                    nextFrontier.append(node.left)
                if node.right:
                    nextFrontier.append(node.right)
            res.append(currSum/count)
            frontier = nextFrontier
        
        return res
