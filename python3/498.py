class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        res = []
        r, c, dr, dc = 0, 0, -1, 1
        while True:
            res.append(mat[r][c])
            if r + c == ROWS + COLS - 2:
                return res
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS:
                r, c = nr, nc
            else:
                if dr == -1:
                    if c + 1 < COLS:
                        c += 1
                    else:
                        r += 1
                else:
                    if r + 1 < ROWS:
                        r += 1
                    else:
                        c += 1
                dr, dc = -dr, -dc
