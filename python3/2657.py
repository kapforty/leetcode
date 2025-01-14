class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        aSet, bSet = set(), set()
        for i in range(len(A)):
            aSet.add(A[i])
            bSet.add(B[i])
            res.append(len(aSet.intersection(bSet)))
        return res
