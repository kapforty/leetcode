class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1,1]]
        if numRows == 1:
            return res[:1]
        if numRows == 2:
            return res
        numRows -= 2
        while numRows > 0:
            temp = [1]
            for i in range(len(res[-1])-1):
                temp.append(res[-1][i] + res[-1][i+1])
            temp.append(1)
            res.append(temp)
            numRows -= 1
        return res
