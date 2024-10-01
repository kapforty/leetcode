class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rMap = defaultdict(int)
        for i in range(len(arr)):
            rMap[arr[i] % k] += 1

        if 0 in rMap:
            if rMap[0] % 2 != 0:
                return False
            del rMap[0]

        for num, count in rMap.items():
            if count != rMap[k - num]:
                return False
        return True
