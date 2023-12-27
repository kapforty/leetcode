class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        color, time = colors[0], neededTime[0]

        for i in range(1,len(colors)):
            if colors[i] != color:
                color, time = colors[i], neededTime[i]
            else:
                res += min(time, neededTime[i])
                time = max(time, neededTime[i])

        return res
            
