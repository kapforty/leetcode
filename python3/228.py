class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        if not nums:
            return 

        curr, count = None, None
        for i in range(len(nums)):
            if not curr:
                curr, count = nums[i], 0
            if i + 1 >= len(nums) or nums[i+1] != curr + 1:
                if count == 0:
                    res.append(str(curr))
                else:
                    res.append(str(curr - count) + "->" + str(curr))
                curr = count = None
            else:
                curr += 1
                count += 1

        return res
                
