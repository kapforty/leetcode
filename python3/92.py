# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# two pass solution w/ stack
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        nums = []
        
        curr, count = head, 1
        while curr:
            if count >= left:
                nums.append(curr.val)
            count += 1
            if count > right:
                break
            curr = curr.next

        curr, count = head, 1
        while curr:
            if count >= left:
                curr.val = nums.pop()
            count += 1
            if count > right:
                break
            curr = curr.next

        return head

# one pass solution
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
            
        dummy = ListNode(0, head)
        count = 0
        start = dummy
        while count < left - 1:
            start = start.next
            count += 1
        end = start.next
        
        count += 1
        prev = start
        curr = start.next
        temp = None
        while count >= left and count <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        
        start.next = prev
        end.next = temp

        return dummy.next