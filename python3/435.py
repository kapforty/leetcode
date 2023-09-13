class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        count = 0

        for fst, snd in intervals[1:]:
            last = res[-1][1]
            if last <= fst:
                res.append([fst, snd])
            else:
                count += 1
                res[-1][1] = min(last, snd)
        
        return count
