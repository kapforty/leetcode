class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0] * max(nums)
        for num in nums:
            arr[num-1] += 1
        prev = curr = 0
        for i in range(len(arr)):
            temp = max(prev + ((i+1)*arr[i]), curr)
            prev = curr
            curr = temp
        return curr
