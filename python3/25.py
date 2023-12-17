# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# --- O(1) SPACE COMPLEXITY ---
# more optimal solution exists, need to code

# --- O(N) SPACE COMPLEXITY ---
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        newValues = []
        while len(values) >= k:
            newValues += values[0:k][::-1]
            values = values[k:]
        newValues += values
        
        curr = head
        for val in newValues:
            curr.val = val
            curr = curr.next

        return head
