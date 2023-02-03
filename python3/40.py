class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def bt(i, currArr, currSum):
            if currSum == target:
                res.append(currArr[::])
                return
            if i >= len(candidates) or currSum > target:
                return
            
            # take candidates[i]
            currArr.append(candidates[i])
            bt(i+1, currArr, currSum + candidates[i])

            # skip candidates[i]
            currArr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            bt(i+1, currArr, currSum)

        bt(0, [], 0)
        return res