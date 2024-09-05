class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        targetSum = mean * (len(rolls) + n)
        for roll in rolls:
            targetSum -= roll

        avg = targetSum / n
        if avg < 1 or avg > 6:
            return []
        avg = floor(avg)
        res = [avg for _ in range(n)]
        targetSum -= avg * n
        
        i = 0
        while targetSum:
            if res[i] == 6:
                i += 1
                continue
            temp = min(targetSum, 6 - res[i])
            res[i] += temp
            targetSum -= temp
        return res
