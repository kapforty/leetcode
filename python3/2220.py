class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # create/format binary strings
        if goal < start:
            start, goal = goal, start
        start, goal = bin(start)[2:], bin(goal)[2:]
        start = "0" * (len(goal) - len(start)) + start
        
        # calculate min flips
        res = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                res += 1
        return res
