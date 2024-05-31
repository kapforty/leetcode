class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        diff = 1
        while diff & xor == 0:
            diff <<= 1

        res = [0, 0]
        for num in nums:
            if diff & num:
                res[0] ^= num
            else:
                res[1] ^= num
                
        return res
