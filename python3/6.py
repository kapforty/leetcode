class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # trivial case
        if numRows == 1:
            return s
            
        # T = down, F = up
        direction = True
        currRow = 0
        strMap = defaultdict(list)

        # map char to row
        for char in s:
            if currRow < 0:
                direction = True
                currRow = 1
            elif currRow >= numRows:
                direction = False
                currRow = numRows - 2
            strMap[currRow].append(char)
            if direction:
                currRow += 1
            else:
                currRow -= 1

        # build result
        res = ""
        for v in strMap.values():
            res += "".join(v)

        return res

