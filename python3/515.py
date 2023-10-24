# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        frontier = deque([root])

        while frontier:
            maxVal = float("-inf")
            for _ in range(len(frontier)):
                curr = frontier.popleft()
                maxVal = max(maxVal, curr.val)
                if curr.left:
                    frontier.append(curr.left)
                if curr.right:
                    frontier.append(curr.right)
            res.append(maxVal)

        return res
