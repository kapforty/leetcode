class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # map num to index
        numToIndex = []
        for i, num in enumerate(nums):
            numToIndex.append((num, i))
        numToIndex.sort()

        # min-heap
        prev, rangeNums, rangeIndices = numToIndex[0][0], [], []
        for num, i in numToIndex:
            if num - prev > limit:
                while rangeNums:
                    currNum, currIdx = heappop(rangeNums), heappop(rangeIndices)
                    nums[currIdx] = currNum
            prev = num
            heappush(rangeNums, num)
            heappush(rangeIndices, i)
        while rangeNums:
            currNum, currIdx = heappop(rangeNums), heappop(rangeIndices)
            nums[currIdx] = currNum
        return nums
