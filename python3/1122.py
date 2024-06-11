class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        appear = set(arr2)
        doNotAppear = []
        arr1Map = defaultdict(int)
        for val in arr1:
            if val in appear:
                arr1Map[val] += 1
            else:
                doNotAppear.append(val)
        doNotAppear.sort()

        res = []
        for val in arr2:
            for i in range(arr1Map[val]):
                res.append(val)
        res += doNotAppear
        return res
