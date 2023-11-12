class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = list(str(x))
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
