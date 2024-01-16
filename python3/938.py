class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        currSum = 0
        def dfs(node):
            nonlocal currSum
            if not node:
                return
            if node.val >= low and node.val <= high:
                currSum += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return currSum
