class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        res = []

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
                if r == 0 or nums[mid-1] < target:
                    break
                r -= 1
            else:
                l = mid + 1

        if nums[r] != target:
            return [-1, -1]
        res.append(r)

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if l == len(nums) - 1 or nums[mid] <= target:
                l = mid
                if nums[mid+1] > target:
                    break
                l += 1
            else:
                r = mid - 1
        res.append(l)

        return res
