class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        curr = points.pop()
        while points:
            temp = points.pop()
            res += max(abs(curr[0] - temp[0]), abs(curr[1] - temp[1]))
            curr = temp
        return res
