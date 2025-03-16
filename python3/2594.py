class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l, r = 1, max(ranks)*cars**2
        def valid(m):
            count = 0
            for r in ranks:
                count += int(sqrt(m/r))
                if count >= cars:
                    return True
            return False
        while l < r:
            m = (l + r) // 2
            if valid(m):
                r = m
            else:
                l = m + 1
        return l
