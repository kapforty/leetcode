# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        currMax = -inf
        count = 1

        queue = [root]

        while queue:
            currSum = self.getSum(queue)
            if currSum > currMax:
                currMax = currSum
                res = count
            newQueue = []

            for node in queue:
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            
            queue = newQueue
            count += 1
        return res

    def getSum(self, nodes):
        currSum = 0
        for node in nodes:
            currSum += node.val
        return currSum
