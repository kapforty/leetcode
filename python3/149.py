class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for x1, y1 in points:
            currMap = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x2 - x1 == 0:
                    if float("inf") in currMap:
                        currMap[float("inf")] += 1
                    else:
                        currMap[float("inf")] = 2
                    continue
                m = (y2-y1)/(x2-x1)
                if m in currMap:
                    currMap[m] += 1
                else:
                    currMap[m] = 2
            if currMap.values():
                res = max(res, max(currMap.values()))
        return res