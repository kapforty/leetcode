class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        dominoMap = defaultdict(int)
        for x, y in dominoes:
            if x > y: x, y = y, x
            res += dominoMap[(x, y)]
            dominoMap[(x, y)] += 1
        return res
