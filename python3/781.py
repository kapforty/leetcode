class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res, counter = 0, Counter(answers)
        for k, v in counter.items():
            temp = ceil(v/(k+1))
            res += temp*(k+1)
        return res
