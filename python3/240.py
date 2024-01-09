class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix) - 1, 0

        while col < len(matrix[0]) and row >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        
        return False
        
