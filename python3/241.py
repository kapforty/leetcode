class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        idx = 1
        res = []
        if len(expression) <= 2:
            return [int(expression)]
        while idx < len(expression):
            if expression[idx] in "+-*":
                left, right = self.diffWaysToCompute(expression[:idx]), self.diffWaysToCompute(expression[idx+1:])
                if expression[idx] == "+":
                    for l in left:
                        for r in right:
                            res.append(l + r)
                elif expression[idx] == "-":
                    for l in left:
                        for r in right:
                            res.append(l - r)
                elif expression[idx] == "*":
                    for l in left:
                        for r in right:
                            res.append(l * r)
            idx += 1
        return res
