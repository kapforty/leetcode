# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # calculate length of linked list
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next

        # do some basic division with remainder, split linked list accordingly
        res = []
        quotient, remainder = length // k, length % k
        prev = curr = head
        while curr:
            res.append(curr)
            for _ in range(quotient):
                prev, curr = curr, curr.next
            if remainder:
                prev, curr = curr, curr.next
                remainder -= 1
            prev.next = None
        while len(res) < k:
            res.append(None)
        return res
