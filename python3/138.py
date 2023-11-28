"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        nodeMap = {}

        # create copies of each node
        curr, ID = head, 0
        while curr:
            nodeMap[ID] = Node(curr.val)
            curr.val = ID
            ID += 1
            curr = curr.next

        # copy pointers from original list
        curr, ID = head, 0
        while curr:
            nodeMap[ID].next = None if not curr.next else nodeMap[curr.next.val]
            nodeMap[ID].random = None if not curr.random else nodeMap[curr.random.val]
            ID += 1
            curr = curr.next

        return nodeMap[0]
