class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0

        for i in range(len(timeSeries)):
            if i+1 <= len(timeSeries) - 1 and timeSeries[i] + duration > timeSeries[i+1]:
                res += timeSeries[i+1] - timeSeries[i]
            else:
                res += duration

        return res
