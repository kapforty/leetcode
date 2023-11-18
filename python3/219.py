class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hashMap and i - hashMap[nums[i]] <= k:
                return True
            hashMap[nums[i]] = i
        return False
