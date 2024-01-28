class Solution:
    def numSplits(self, s: str) -> int:
        res = 0
        leftMap, rightMap = defaultdict(int), defaultdict(int)
        for char in s:
            rightMap[char] += 1
        
        for char in s:
            leftMap[char] += 1
            rightMap[char] -= 1
            if rightMap[char] == 0:
                del rightMap[char]
            if len(leftMap.keys()) == len(rightMap.keys()):
                res += 1
        
        return res
