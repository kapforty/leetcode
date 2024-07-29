class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = float("inf")
        numBOnLeft = [0 for _ in range(len(s))]
        countA = countB = 0
        for i in range(len(s)):
            numBOnLeft[i] = countB
            if s[i] == "b":
                countB += 1
        for i in range(len(s)-1, -1, -1):
            res = min(numBOnLeft[i] + countA, res)
            if s[i] == "a":
                countA += 1
        return res
