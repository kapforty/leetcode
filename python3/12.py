class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        numMap = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

        while num > 0:
            for k, v in numMap.items():
                if k <= num:
                    res += v
                    num -= k
                    break
        
        return res
        
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         romanNums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
#         instances = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        
#         res = ""
#         nums = []

#         nums = list(str(num))
        
#         multi = 1
#         for i in range(len(nums) - 1, - 1, -1):
#             nums[i] = multi * int(nums[i])
#             multi *= 10

#         for curr in nums:
#             if curr in instances:
#                 res += instances[curr]
#                 continue

#             currStr = ""
#             while curr > 0:
#                 for k, v in romanNums.items():
#                     if v <= curr:
#                         currStr += k
#                         curr -= v
#                         break
#             res += currStr

#         return res
