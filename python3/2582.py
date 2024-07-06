class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1
        curr = 1
        while time:
            if curr == 1 or curr == n:
                direction = -direction
            curr += direction
            time -= 1
        return curr
