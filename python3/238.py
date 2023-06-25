class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        prefix, postfix = 1, 1
        for i in range(0, len(nums), 1):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res



        # --- O(N) RUNTIME, O(N) SPACE COMPLEXITY ---
        # arr1, arr2 = nums.copy(), nums.copy()
        # arr1.insert(0, 1)
        # arr2.append(1)
        
        # for i in range(1, len(arr1), 1):
        #     arr1[i] = arr1[i] * arr1[i-1]
        
        # for i in range(len(arr2)-2, -1, -1):
        #     arr2[i] = arr2[i] * arr2[i+1]

        # res = []
        # for i in range(len(nums)):
        #     res.append(arr1[i] * arr2[i+1])
        # return res
