class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        freqs = [[] for _ in range(len(nums)+1)]
        for key, val in hashmap.items():
            freqs[val].append(key)

        res = []
        for arr in freqs[::-1]:
            for num in arr:
                res.append(num)
                if len(res) == k:
                    return res
