class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def checkFlowers(days):
            flowers = bouquets = 0
            for flower in bloomDay:
                flowers = flowers + 1 if flower <= days else 0
                if flowers == k:
                    flowers = 0
                    bouquets += 1
                    if bouquets == m:
                        return True
            return False

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            days = (l + r) // 2
            if not checkFlowers(days):
                l = days + 1
            else:
                r = days

        return l
    
