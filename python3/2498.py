class Solution:
    def maxJump(self, stones: List[int]) -> int:
        up, down = [], []
        for i in range(0, len(stones),2):
            up.append(stones[i])
        for i in range(1, len(stones), 2):
            down.append(stones[i])
        final = up + down[::-1]

        res = float("-inf")
        for i in range(len(stones)-1):
            res = max(res, abs(final[i] - final[i+1]))
        return res
