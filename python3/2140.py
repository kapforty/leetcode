class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)
        for i in range(len(questions)):
            dp[i] = max(dp[i], dp[i-1])
            points, brainpower = questions[i]
            if i + brainpower >= len(questions):
                dp[-1] = max(dp[-1], dp[i] + points)
            else:
                dp[i+brainpower+1] = max(dp[i+brainpower+1], dp[i] + points)
        return dp[-1]
