class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = points[0]
        SIZE = len(res)
        for row in points[1:]:
            for i in range(SIZE):
                diff = 1
                while i - diff >= 0 and res[i] - diff > res[i - diff]:
                    res[i - diff] = res[i] - diff
                    diff += 1
                diff = 1
                while i + diff < SIZE and res[i] - diff > res[i + diff]:
                    res[i + diff] = res[i] - diff
                    diff += 1
            for i in range(SIZE):
                res[i] += row[i]
        return max(res)
