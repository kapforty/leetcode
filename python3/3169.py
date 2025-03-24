class Solution:
    def overlap(self, int1, int2):
        s1, e1 = int1
        s2, e2 = int2
        if e1 < s2 or e2 < s1:
            return False
        return True
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        res = []
        meetings.sort(key=lambda x: x[1])
        while len(meetings) >= 2:
            if not self.overlap(meetings[-1], meetings[-2]):
                res.append(meetings.pop())
            else:
                s = min(meetings[-1][0], meetings[-2][0])
                e = max(meetings[-1][1], meetings[-2][1])
                meetings.pop()
                meetings[-1] = [s, e]
        res.append(meetings.pop())
        for x, y in res:
            days -= y - x + 1
        return days
