class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        def bt(row, invalidCols, invalidDiagonals, invalidDiagonals2):
            nonlocal res
            if row == n:
                res += 1
                return
            for col in range(n):
                if col in invalidCols or row - col in invalidDiagonals or row + col in invalidDiagonals2:
                    continue
                invalidCols.add(col)
                invalidDiagonals.add(row - col)
                invalidDiagonals2.add(row + col)
                bt(row + 1, invalidCols, invalidDiagonals, invalidDiagonals2)
                invalidCols.remove(col)
                invalidDiagonals.remove(row - col)
                invalidDiagonals2.remove(row + col)
                
        bt(0, set(), set(), set())
        return res
