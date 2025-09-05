class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for r in range(1, 61):
            question = num1 - (r * num2)
            if question.bit_count() <= r <= question:
                return r
        return -1
