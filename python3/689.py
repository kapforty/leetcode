class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        window_sum = [0] * (n - k + 1)
        
        current_sum = sum(nums[:k])
        window_sum[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = current_sum
        
        left = [0] * len(window_sum)
        best_left = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best_left]:
                best_left = i
            left[i] = best_left
        
        right = [0] * len(window_sum)
        best_right = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best_right]:
                best_right = i
            right[i] = best_right
        
        max_sum = 0
        result = []
        for mid in range(k, len(window_sum) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = window_sum[l] + window_sum[mid] + window_sum[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]
        
        return result
