class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(land), len(land[0])
        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c] == 0:
                    continue

                # check if current position is top left corner of farmland
                if not ((r - 1 < 0 or land[r - 1][c] == 0) and (c - 1 < 0 or land[r][c - 1] == 0)):
                    continue

                # calculate the bottom right coordinates
                r2, c2 = r, c
                while r2 + 1 < ROWS and land[r2 + 1][c2] == 1:
                    r2 += 1
                while c2 + 1 < COLS and land[r2][c2 + 1] == 1:
                    c2 += 1

                # add coordinates to result
                res.append([r, c, r2, c2])
        return res
