# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swaps(self, arr) -> int:
        sortedArr = []
        for i, val in enumerate(arr):
            sortedArr.append((val, i))
        sortedArr.sort()
        swaps, visited = 0, set()
        for idx in range(len(sortedArr)):
            val, i = sortedArr[idx]
            if idx == i or i in visited:
                continue
            while i not in visited:
                swaps += 1
                visited.add(i)
                i = sortedArr[i][1]
            swaps -= 1
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res, frontier = 0, [root]
        while frontier:
            nextFrontier, arr = [], []
            for node in frontier:
                if node.left:
                    nextFrontier.append(node.left)
                    arr.append(node.left.val)
                if node.right:
                    nextFrontier.append(node.right)
                    arr.append(node.right.val)
            res += self.swaps(arr)
            frontier = nextFrontier
        return res
