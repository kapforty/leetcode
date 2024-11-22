class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        mapski = defaultdict(int)
        for row in matrix:
            curr = "".join([str(val) for val in row])
            invCurr = ""
            for c in curr:
                invCurr += "1" if c == "0" else "0"
            mapski[curr] += 1
            mapski[invCurr] += 1
        return max(mapski.values())