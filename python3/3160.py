class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res, counts, idxToColor = [], defaultdict(int), defaultdict(int)
        for x, y in queries:
            if x in idxToColor:
                counts[idxToColor[x]] -= 1
                if counts[idxToColor[x]] == 0:
                    del counts[idxToColor[x]]
            idxToColor[x] = y
            counts[y] += 1
            res.append(len(counts))
        return res
