class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodeMap = defaultdict(int)

        def dfs(node):
            if not node:
                return
            nodeMap[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        maxi = max(nodeMap.values())
        res = []
        for k, v in nodeMap.items():
            if v == maxi:
                res.append(k)
        return res
