class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = count = l = r = 0
        tracker = defaultdict(int)
        while r < len(nums):
            temp = str(bin(nums[r]))[2:][::-1]
            r += 1
            for i, c in enumerate(temp):
                if c == "1":
                    tracker[i] += 1
                    if tracker[i] > 1:
                        count += 1
            while count > 0:
                temp = str(bin(nums[l]))[2:][::-1]
                l += 1
                for i, c in enumerate(temp):
                    if c == "1":
                        tracker[i] -= 1
                        if tracker[i] == 1:
                            count -= 1
            res = max(res, r - l)
        return res
