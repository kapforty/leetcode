# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        masterHead = ListNode(101, head)
        prev = masterHead
        while head and head.next:
            if head.val != head.next.val:
                prev = head
                head = head.next
            else:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
                head.next = None
                head = prev.next
        return masterHead.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # calculate counts
        counts = defaultdict(int)
        curr = head
        while curr:
            counts[curr.val] += 1
            curr = curr.next

        # find which nodes to remove
        remove = set()
        for k, v in counts.items():
            if v > 1:
                remove.add(k)
        
        # remove nodes
        head = ListNode(101, head)
        prev, curr = head, head.next
        while curr:
            if curr.val in remove:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return head.next

        
        
