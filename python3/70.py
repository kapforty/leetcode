class Solution:
    def climbStairs(self, n: int) -> int:
        numPaths = [0 for _ in range(n+2)]
        numPaths[0] = 1

        for i in range(n):
            numPaths[i+1] += numPaths[i]
            numPaths[i+2] += numPaths[i]
        
        return numPaths[n]
