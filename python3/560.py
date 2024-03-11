class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] += 1
        res = 0
        curr = 0
        for val in nums:
            curr += val
            res += prefixMap[curr - k]
            prefixMap[curr] += 1
        return res