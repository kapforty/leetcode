class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        starts, ends = [], []
        for s, e, v in events:
            starts.append((s, v))
            ends.append((e, v))
        starts.sort(reverse=True)
        ends.sort(reverse=True)

        res = maxVal = 0
        while starts and ends:
            if ends[-1][0] >= starts[-1][0]:
                res = max(res, starts[-1][1] + maxVal)
                starts.pop()
            elif ends[-1][0] < starts[-1][0]:
                maxVal = max(maxVal, ends[-1][1])
                res = max(res, starts[-1][1] + maxVal)
                ends.pop()
        while ends:
            res = max(res, ends.pop()[1])
        return res
