class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []

        for kid in candies:
            if kid + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)

        return res
