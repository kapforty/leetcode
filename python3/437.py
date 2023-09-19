# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        def dfs(node, total):
            count = 0
            if node:
                total += node.val
                count = prefixSum[total - targetSum]
                prefixSum[total] += 1
                count += dfs(node.left, total) + dfs(node.right, total)
                prefixSum[total] -= 1
            return count

        return dfs(root, 0)
