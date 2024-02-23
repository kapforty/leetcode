class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(left, right, curr):
            if left == right == 0:
                res.append(curr)
                return
            if left > 0:
                helper(left-1, right, curr + "(")
            if right > 0 and left < right:
                helper(left, right-1, curr + ")")
        helper(n, n, "")
        
        return res
