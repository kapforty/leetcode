# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # turn listNode values into array
        numArray = []
        for listNode in lists:
            while listNode:
                numArray.append(listNode.val)
                listNode = listNode.next
        
        # sort array
        numArray.sort()

        # make new listNode from sorted array
        res = ptr = ListNode()
        for n in numArray:
            temp = ListNode(n, None)
            ptr.next = temp
            ptr = ptr.next
        
        return res.next
