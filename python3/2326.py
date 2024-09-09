# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top, bottom, left, right = 1, m - 1, 0, n - 1
        res = [[-1 for _ in range(n)] for _ in range(m)]
        r = c = direction = 0
        while head:
            res[r][c] = head.val
            head = head.next

            # check bounds
            if direction == 0 and c == right:
                direction = 1
                right -= 1
            elif direction == 1 and r == bottom:
                direction = 2
                bottom -= 1
            elif direction == 2 and c == left:
                direction = 3
                left += 1
            elif direction == 3 and r == top:
                direction = 0
                top += 1

            # move position
            if direction == 0:
                c += 1
            elif direction == 1:
                r += 1
            elif direction == 2:
                c -= 1
            else:
                r -= 1
                
        return res
