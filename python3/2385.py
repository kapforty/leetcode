# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjMatrix = defaultdict(list)

        # populate adjacency matrix
        def dfs(node, parent):
            if not node:
                return
            adjMatrix[node.val].append(parent.val)
            adjMatrix[parent.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root.left, root)
        dfs(root.right, root)

        # run bfs from start
        visited = set()
        visited.add(start)
        frontier = [start]
        res = -1
        while frontier:
            res += 1
            temp = []
            for node in frontier:
                for neighbor in adjMatrix[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        temp.append(neighbor)
            frontier = temp
        
        return res
        
