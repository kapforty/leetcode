class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr = [0]
        for num in nums:
            nextCurr = []
            for n in curr:
                nextCurr.append(n + num)
                nextCurr.append(n - num)
            curr = nextCurr
        return curr.count(target)
