class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        oddEven = evenOdd = evenEven = oddOdd = 0
        for num in nums:
            if num % 2:
                oddOdd += 1
                oddEven = max(oddEven, evenOdd + 1)
            else:
                evenEven += 1
                evenOdd = max(evenOdd, oddEven + 1)
        return max(oddEven, evenOdd, evenEven, oddOdd)
