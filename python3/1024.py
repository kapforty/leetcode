class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # sort/clean clips
        clips.sort()
        while clips and clips[-1][0] >= time:
            clips.pop()
        for i in range(len(clips)):
            clips[i][1] = min(time, clips[i][1])
        
        # setup dp array
        dp = [float("inf") for _ in range(time + 1)]
        if not clips or clips[0][0] != 0:
            return -1
        for i in range(clips[0][1] + 1):
            dp[i] = 1
        dp[0] = 0
        
        # dp
        for start, end in clips[1:]:
            end = min(end, time)
            if dp[start] == float("inf"):
                return -1
            for i in range(start, end + 1):
                dp[i] = min(dp[i], dp[start] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1
