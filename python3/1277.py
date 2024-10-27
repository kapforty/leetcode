class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    continue
                frontier = set()
                frontier.add((r,c))
                while frontier:
                    res += 1
                    nextFrontier = set()
                    for row, col in frontier:
                        if row + 1 >= ROWS or col + 1 >= COLS or matrix[row+1][col] == 0 or matrix[row][col+1] == 0 or matrix[row+1][col+1] == 0:
                            nextFrontier = set()
                            break
                        nextFrontier.add((row+1, col))
                        nextFrontier.add((row, col+1))
                        nextFrontier.add((row+1, col+1))
                    frontier = nextFrontier
        return res
