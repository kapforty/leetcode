class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            curr = str(i)
            if len(curr) % 2:
                continue
            left = right = 0
            for j in range(len(curr)//2):
                left += int(curr[j])
            for j in range(len(curr)//2, len(curr)):
                right += int(curr[j])
            if left == right:
                res += 1
        return res
