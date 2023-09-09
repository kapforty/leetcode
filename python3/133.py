"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            copy = Node(node.val)
            nodeMap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None

    
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return None
            
#         queue = [node]
#         visited = set()
#         nodeMap = {}
        
#         while queue:
#             curr = queue.pop(0)
#             if curr not in nodeMap:
#                 nodeMap[curr] = Node(curr.val)
#             for neighbor in curr.neighbors:
#                 if neighbor not in visited and neighbor not in queue:
#                     queue.append(neighbor)
#                 if neighbor not in nodeMap:
#                     nodeMap[neighbor] = Node(neighbor.val)
#                 nodeMap[curr].neighbors.append(nodeMap[neighbor])
#             visited.add(curr)
        
#         return nodeMap[node]
