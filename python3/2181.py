# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, tail = head.next, head
        currSum = 0
        while curr:
            if curr.val == 0:
                tail.val = currSum
                currSum = 0
                if curr.next != None:
                    tail = tail.next
            else:
                currSum += curr.val
            curr = curr.next
        tail.next = None
        return head
