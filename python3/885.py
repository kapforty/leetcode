class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        stepSize = 1

        def updateRes():
            if rStart < 0 or cStart < 0 or rStart >= rows or cStart >= cols:
                return
            res.append([rStart, cStart])

        while len(res) < rows * cols:
            if stepSize % 2 != 0:
                for _ in range(stepSize):
                    cStart += 1
                    updateRes()
                for _ in range(stepSize):
                    rStart += 1
                    updateRes()
            else:
                for _ in range(stepSize):
                    cStart -= 1
                    updateRes()
                for _ in range(stepSize):
                    rStart -= 1
                    updateRes()
            stepSize += 1

        return res
