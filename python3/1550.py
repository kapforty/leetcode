class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        for num in arr:
            if num % 2 == 1:
                odd += 1
                if odd == 3:
                    return True
            else:
                odd = 0
        return False
