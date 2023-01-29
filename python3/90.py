class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(idx, currArr):
            if idx == len(nums):
                res.append(currArr.copy())
                return
            currArr.append(nums[idx])
            bt(idx+1, currArr)
            currArr.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            bt(idx+1, currArr)

        bt(0, [])
        return res