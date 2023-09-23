class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = ceil(sum(piles)/h), max(piles)
        
        while l < r:
            speed = (l + r) // 2
            hrs = 0
            for pile in piles:
                hrs += ceil(pile/speed)
            if hrs <= h:
                r = speed
            else:
                l = speed + 1

        return l
