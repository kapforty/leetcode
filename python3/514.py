class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        for char in key[::-1]:
            temp = [float("inf")] * len(ring)
            for i in range(len(ring)):
                for j in range(len(ring)):
                    if ring[j] == char:
                        mini = min(abs(i - j), len(ring) - abs(i - j))
                        temp[i] = min(temp[i], mini + dp[j])
            dp = temp
        return dp[0] + len(key)
                
