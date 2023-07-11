# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # --- O(N) TIME COMPLEXITY, O(N) SPACE COMPLEXITY ---
        length = 0
        idx = 0
        nodeMap = {}

        # calculate length of listNode, map index to node pointers
        ptr = head
        while ptr:
            nodeMap[idx] = ptr
            length += 1
            idx += 1
            ptr = ptr.next

        # node to remove is first
        if length - n == 0:
            return head.next

        # node to remove is last
        if n == 1:
            nodeMap[length-n-1].next = None
            return head

        # node before and after node to remove exist
        nodeMap[length-n-1].next = nodeMap[length-n+1]
        return head

        # --- O(N) TIME COMPLEXITY, O(1) SPACE COMPLEXITY ---
        # dummy = ListNode(-1, head)
        # left, right = dummy, head

        # while n > 0:
        #     right = right.next
        #     n -= 1
        
        # while right:
        #     left = left.next
        #     right = right.next

        # left.next = left.next.next
        # return dummy.next

        
        

        
        
