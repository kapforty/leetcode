class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixMap = defaultdict(int)
        prefixMap[0] += 1
        curr = res = 0
        for val in nums:
            curr += val
            res += prefixMap[curr - goal]
            prefixMap[curr] += 1
        return res