class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupes = set()
        writeIndex = 0

        for i in range(len(nums)):
            if nums[i] in dupes:
                continue
            nums[writeIndex] = nums[i]
            writeIndex += 1
            dupes.add(nums[i])

        return len(dupes)
