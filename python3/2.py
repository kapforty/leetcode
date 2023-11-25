# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        tail = head
        while l1 is not None or l2 is not None or carry != 0:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            newVal = val1 + val2 + carry
            tail.next = ListNode(newVal % 10)
            carry = newVal // 10

            tail = tail.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head.next
