class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = [0 for _ in range(len(matrix[0]))]
                continue
            for j in range(len(matrix[0])):
                if j in cols:
                    matrix[i][j] = 0

        return matrix
