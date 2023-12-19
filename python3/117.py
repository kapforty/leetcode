"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        frontier = [root]
        while frontier:
            temp = []
            fLen = len(frontier)
            for i in range(fLen):
                curr = frontier[i]
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
                if i == fLen - 1:
                    break
                curr.next = frontier[i + 1]
            frontier = temp
        return root
