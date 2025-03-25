class Solution:
    def overlap(self, int1, int2):
        s1, e1 = int1
        s2, e2 = int2
        if e1 <= s2 or e2 <= s1:
            return False
        return True

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xIntervals, yIntervals, xMerged, yMerged = [], [], [], []
        for x1, y1, x2, y2 in rectangles:
            xIntervals.append([x1, x2])
            yIntervals.append([y1, y2])
        xIntervals.sort(key=lambda x: x[1])
        yIntervals.sort(key=lambda x: x[1])
        
        while len(xIntervals) > 1:
            curr = xIntervals.pop()
            if self.overlap(curr, xIntervals[-1]):
                s1, e1 = curr
                s2, e2 = xIntervals[-1]
                s, e = min(s1, s2), max(e1, e2)
                xIntervals[-1] = [s, e]
            else:
                xMerged.append(curr)
        xMerged.append(xIntervals.pop())
        while len(yIntervals) > 1:
            curr = yIntervals.pop()
            if self.overlap(curr, yIntervals[-1]):
                s1, e1 = curr
                s2, e2 = yIntervals[-1]
                s, e = min(s1, s2), max(e1, e2)
                yIntervals[-1] = [s, e]
            else:
                yMerged.append(curr)
        yMerged.append(yIntervals.pop())

        return len(xMerged) > 2 or len(yMerged) > 2
