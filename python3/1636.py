class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        freqMap = defaultdict(list)
        res = []
        for k, v in counter.items():
            freqMap[v].append(k)
        keys = sorted(freqMap.keys())
        for key in keys:
            vals = sorted(freqMap[key], reverse=True)
            for val in vals:
                for _ in range(key):
                    res.append(val)
        return res
