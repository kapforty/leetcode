class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, big, small):
            nonlocal res
            if not node:
                return
            big = max(big, node.val)
            small = min(small, node.val)
            res = max(res, big-small)
            dfs(node.left, big, small)
            dfs(node.right, big, small)
        
        dfs(root, root.val, root.val)
        return res
