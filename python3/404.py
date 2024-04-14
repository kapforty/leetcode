class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, isLeft):
            nonlocal res
            if not node:
                return
            if not node.left and not node.right and isLeft:
                res += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root, False)
        return res
