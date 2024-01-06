class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res, curr = -1, 0
        for i in range(len(gas)):
            ev = gas[i] - cost[i]
            if ev >= curr + ev:
                res = i
            curr = max(curr + ev, ev)

        return res

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
