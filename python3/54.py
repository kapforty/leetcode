class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = {"right": (0,1), "left": (0,-1), "down": (1,0), "up": (-1,0)}
        direction = "right"
        leftBound, rightBound, topBound, bottomBound = -1, len(matrix[0]), -1, len(matrix)
        row, col = 0, 0

        res = []
        while rightBound - leftBound > 1 and bottomBound - topBound > 1:
            res.append(matrix[row][col])
            if direction == "right" and col + 1 == rightBound:
                topBound += 1
                direction = "down"
            elif direction == "down" and row + 1 == bottomBound:
                rightBound -= 1
                direction = "left"
            elif direction == "left" and col - 1 == leftBound:
                bottomBound -= 1
                direction = "up"
            elif direction == "up" and row - 1 == topBound:
                leftBound += 1
                direction = "right"
            row += directions[direction][0]
            col += directions[direction][1]
        
        return res
