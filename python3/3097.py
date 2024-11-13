class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # track occurrences of 1's for each bit position
        curr = [0] * 30
        def convertToDecimal():
            bitstring = ""
            for num in curr:
                if num > 0:
                    bitstring += "1"
                else:
                    bitstring += "0"
            return int(bitstring, 2)

        # sliding window
        res = inf
        l = r = 0
        while r < len(nums):
            if convertToDecimal() < k:
                n = str(bin(nums[r]))[2:]
                for i, bit in enumerate(n):
                    if bit == "1":
                        curr[30 - len(n) + i] += 1
                r += 1
            else:
                if l == r:
                    return 1
                res = min(res, r - l)
                n = str(bin(nums[l]))[2:]
                for i, bit in enumerate(n):
                    if bit == "1":
                        curr[30 - len(n) + i] -= 1
                l += 1

        # slide left side of window up
        while convertToDecimal() >= k:
            res = min(res, r - l)
            n = str(bin(nums[l]))[2:]
            for i, bit in enumerate(n):
                if bit == "1":
                    curr[30 - len(n) + i] -= 1
            l += 1

        # return result
        return -1 if res == inf else res
                
