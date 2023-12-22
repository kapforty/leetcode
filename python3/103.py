# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return

        res = []
        frontier = [root]
        while frontier:
            temp, newFrontier = [], []
            for node in frontier:
                temp.append(node.val)
                if node.left:
                    newFrontier.append(node.left)
                if node.right:
                    newFrontier.append(node.right)
            res.append(temp)
            frontier = newFrontier
        
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res
