# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = curr = head

        if head.val * 2 > 9:
            newHead = ListNode(0, head)
            head = prev = newHead

        while curr:
            temp = curr.val * 2
            if temp > 9:
                prev.val += 1
            curr.val = temp % 10
            prev = curr
            curr = curr.next
        
        return head
