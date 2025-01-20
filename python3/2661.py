class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # map row/col to unpainted cells
        ROWS, COLS = len(mat), len(mat[0])
        rowMap, colMap = {}, {}
        for r in range(ROWS):
            rowMap[r] = COLS
        for c in range(COLS):
            colMap[c] = ROWS
        
        # map cell number to row/col
        coordinates = {}
        for r in range(ROWS):
            for c in range(COLS):
                coordinates[mat[r][c]] = (r, c)

        # iterate through arr
        for i, curr in enumerate(arr):
            r, c = coordinates[curr]
            rowMap[r] -= 1
            colMap[c] -= 1
            if rowMap[r] == 0 or colMap[c] == 0:
                return i
