# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        leftTail, rightTail = left, right

        curr = head
        while curr:
            temp = curr.next
            if curr.val < x:
                leftTail.next = curr
                leftTail = curr
            else:
                rightTail.next = curr
                rightTail = curr
            curr = temp

        leftTail.next = right.next
        rightTail.next = None

        return left.next
