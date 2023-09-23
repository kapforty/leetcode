class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        letters = {"2": "abc", "3": "def", "4": "ghi",  "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def backtrack(string, nextDigits):
            if not nextDigits:
                res.append(string)
                return
            for letter in letters[nextDigits[0]]:
                backtrack(string + letter, nextDigits[1:])

        backtrack("", digits)
        return res
            
# ITERATIVE
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         letters = {"2": "abc", "3": "def", "4": "ghi",  "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#         res = []

#         for char in digits:
#             if not res:
#                 res = letters[char]
#                 continue
   
#             temp = []
#             for string in res:
#                 for letter in letters[char]:
#                     temp.append(string + letter)
#             res = temp

#         return res
