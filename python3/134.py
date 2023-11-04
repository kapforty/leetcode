class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        res, currSum = 0, 0

        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
            if currSum < 0:
                res = i
                currSum = 0
            currSum += diff[i]
        
        return res if sum(diff) >= 0 else -1
