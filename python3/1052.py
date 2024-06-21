class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = 0
        for i in range(len(grumpy)):
            if not grumpy[i]:
                res += customers[i]
        
        curr, ptr = res, 0
        for i in range(minutes):
            if grumpy[ptr]:
                curr += customers[ptr]
            ptr += 1
        res = max(res, curr)

        while ptr < len(grumpy):
            if grumpy[ptr - minutes]:
                curr -= customers[ptr - minutes]
            if grumpy[ptr]:
                curr += customers[ptr]
            res = max(res, curr)
            ptr += 1
        
        return res
