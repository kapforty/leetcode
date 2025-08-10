class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        curr, counter = 1, Counter(str(n))
        while curr < 9999999999:
            if counter == Counter(str(curr)):
                return True
            curr *= 2
        return False
