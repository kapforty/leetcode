# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
          return head

        # calculate length of linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # calculate new value for k
        k = k % length
        if not k:
          return head
        k = length - k

        # make rotation
        prev, curr = None, head
        for _ in range(k):
            prev = curr
            curr = curr.next
        while curr.next:
            curr = curr.next
        curr.next = head
        head = prev.next
        prev.next = None

        return head
