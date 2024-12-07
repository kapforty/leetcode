class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        res = currSum = 0
        for i in range(n):
            if currSum + i + 1 > maxSum:
                break
            if i + 1 not in banned:
                res += 1
                currSum += i + 1
        return res
