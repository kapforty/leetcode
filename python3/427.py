"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
          
        # divide and conquer
        def dnq(left, right, top, bottom):
            checkLeaf = isLeaf(left, right, top, bottom)
            if checkLeaf[0]:
                return Node(checkLeaf[1], True, None, None, None, None)
            else:
                return Node(False, False, 
                    dnq(left, (left+right)//2, top, (top+bottom)//2), 
                    dnq((left+right)//2, right, top, (top+bottom)//2), 
                    dnq(left, (left+right)//2, (top+bottom)//2, bottom), 
                    dnq((left+right)//2, right, (top+bottom)//2, bottom))

        # check for leaf/val
        def isLeaf(left, right, top, bottom):
            hasZero, hasOne = False, False
            for row in range(top, bottom):
                for col in range(left, right):
                    if grid[row][col] == 0:
                        hasZero = True
                    if grid[row][col] == 1:
                        hasOne = True
                    if hasZero and hasOne:
                        return [False, False]
            return [True, hasOne]

        return dnq(0, len(grid[0]), 0, len(grid))
