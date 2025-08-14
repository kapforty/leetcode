# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # build lists of nodes
        stackA, stackB = [], []
        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next
        
        # find intersection
        res = None
        if stackA[-1] != stackB[-1]:
            return res
        while stackA and stackB and stackA[-1] == stackB[-1]:
            res = stackA[-1]
            stackA.pop()
            stackB.pop()
        return res
