class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                res.append((arr[i]/arr[j], [arr[i], arr[j]]))
        res.sort()
        return res[k-1][1]