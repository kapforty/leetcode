class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert timePoints into minutes
        minutes = []
        for point in timePoints:
            minutes.append(int(point[:2]) * 60 + int(point[3:]))
        minutes.sort()
        
        # calculate result
        res = abs(minutes[-1] - 1440 - minutes[0])
        for i in range(len(minutes) - 1):
            res = min(res, minutes[i + 1] - minutes[i])
        return res
