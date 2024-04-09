class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i in range(len(tickets)):
            if i > k and tickets[k] <= tickets[i]:
                res += min(tickets[k]-1, tickets[i])
            else:
                res += min(tickets[k], tickets[i])
        return res
