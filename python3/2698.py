class Solution:
    def valid(self, target, remaining):
        if target == 0 and remaining == "":
            return True
        if target < 0:
            return False
        for i in range(1, len(remaining) + 1):
            if self.valid(target - int(remaining[:i]), remaining[i:]):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            if self.valid(i, str(i**2)):
                res += i**2
        return res
