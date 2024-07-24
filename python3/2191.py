class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappings = defaultdict(list)
        keys = set()
        for num in nums:
            numStr = str(num)
            mappedStr = ""
            for char in numStr:
                mappedStr += str(mapping[int(char)])
            mappings[int(mappedStr)].append(num)
            keys.add(int(mappedStr))
        keys = list(keys)
        keys.sort()
        
        res = []
        for key in keys:
            res += mappings[key]
        return res
