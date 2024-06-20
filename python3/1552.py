class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(dist):
            balls, prev = 0, float("-inf")
            for pos in position:
                if pos - prev >= dist:
                    balls += 1
                    if balls == m:
                        return True
                    prev = pos
            return False

        l, r = 1, position[-1] - position[0]
        count = 0
        while l < r:
            mid = ceil((l + r) / 2)
            if check(mid):
                l = mid
            else:
                r = mid - 1
        
        return l
