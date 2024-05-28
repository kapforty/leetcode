class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        l = r = currSum = res = 0
        while l < len(costs):
            while r < len(costs) and currSum + costs[r] <= maxCost:
                currSum += costs[r]
                r += 1
            res = max(res, r - l)
            currSum -= costs[l]
            l += 1
        return res
