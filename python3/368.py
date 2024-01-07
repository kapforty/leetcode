class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        mapski = defaultdict(list)
        
        for num in nums:
            for k in mapski.copy().keys():
                if num % k == 0:
                    if num not in mapski:
                        mapski[num] = mapski[k] + [num]
                        continue
                    if len(mapski[k]) + 1 > len(mapski[num]):
                        mapski[num] = mapski[k] + [num]  
            if num not in mapski: 
                mapski[num] = [num]
        
        res = None
        count = 0
        for v in mapski.values():
            if len(v) > count:
                count = len(v)
                res = v
        return res
