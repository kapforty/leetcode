class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        
        for temp in temperatures[::-1]:
            days = 1
            while stack and stack[-1][0] <= temp:
                poppedTemp = stack.pop()
                days += poppedTemp[1]
            if stack:
                res.append(days)
                stack.append((temp, days))
            else:
                res.append(0)
                stack.append((temp, 0))

        return res[::-1]
