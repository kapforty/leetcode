class Solution:
    def minSteps(self, s: str, t: str) -> int:
        charsS, charsT = defaultdict(int), defaultdict(int)
        for char in s:
            charsS[char] += 1
        for char in t:
            charsT[char] += 1
        
        res = 0
        for k in charsT.keys():
            if charsT[k] > charsS[k]:
                res += charsT[k] - charsS[k]

        return res
