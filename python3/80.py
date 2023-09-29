class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        count = 0
        writeIdx = 0

        for i in range(len(nums)):
            if nums[i] == prev:
                if count >= 2:
                    continue
                else:
                    count += 1
                    nums[writeIdx] = nums[i]
                    writeIdx += 1
            else:
                prev = nums[i]
                count = 1
                nums[writeIdx] = nums[i]
                writeIdx += 1
        
        return writeIdx
