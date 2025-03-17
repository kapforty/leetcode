class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for k, v in counter.items():
            if v % 2 != 0:
                return False
        return True
