class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # count occurrences
        counts = [0 for _ in range(len(grid)**2)]
        for r in range(len(grid)):
            for c in range(len(grid)):
                counts[grid[r][c] - 1] += 1
        
        # find missing and repeated values
        res = [None, None]
        for k, v in enumerate(counts):
            if v == 0:
                res[1] = k + 1
            elif v == 2:
                res[0] = k + 1
        return res
