class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits.count(9) == len(digits):
            return [1] + [0 for i in range(len(digits))]
        
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] >= 10:
                digits[i] -= 10
                digits[i-1] += 1
        
        return digits
