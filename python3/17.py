class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        numMap = {
            "1" : [],
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        res = []
        def bt(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for char in numMap[digits[i]]:
                bt(i+1, curr + char)
        bt(0, "")
        return res
