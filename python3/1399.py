class Solution:
    def countLargestGroup(self, n: int) -> int:
        groupMap = defaultdict(int)
        for i in range(n):
            curr, currSum = str(i + 1), 0
            for c in curr:
                currSum += int(c)
            groupMap[currSum] += 1
        res = maxSize = -1
        for k, v in groupMap.items():
            if v > maxSize:
                res, maxSize = 1, v
            elif v == maxSize:
                res += 1
        return res
