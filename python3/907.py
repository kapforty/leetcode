class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left, right = [], []
        stack = []
        for val in arr:
            count = 1
            while stack and stack[-1][0] >= val:
                curr = stack.pop()
                count += curr[1]
            stack.append((val, count))
            left.append(count)
        stack = []
        for val in arr[::-1]:
            count = 1
            while stack and stack[-1][0] > val:
                curr = stack.pop()
                count += curr[1]
            stack.append((val, count))
            right.append(count)
        right = right[::-1]

        res = 0
        for i in range(len(arr)):
            res += arr[i] * left[i] * right[i]
        return res % (10**9 + 7)
        
