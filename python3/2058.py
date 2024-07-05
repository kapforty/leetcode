# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalPoints = []
        prev, curr = head, head.next
        i = 1
        while curr.next:
            if (curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val):
                criticalPoints.append(i)
            prev = curr
            curr = curr.next
            i += 1
        if len(criticalPoints) < 2:
            return [-1, -1]
        res = [criticalPoints[-1] - criticalPoints[0], criticalPoints[-1] - criticalPoints[0]]
        for i in range(len(criticalPoints) - 1):
            res[0] = min(res[0], criticalPoints[i+1] - criticalPoints[i])
        return res

