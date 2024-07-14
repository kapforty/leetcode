class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxFreq = res = 0
        for k, v in counter.items():
            if v > maxFreq:
                maxFreq = v
                res = 0
                res += v
            elif v == maxFreq:
                res += v
        return res
