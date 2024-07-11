class Solution:
    def reverseParentheses(self, s: str) -> str:
        res, stack = "", []
        for char in s:
            if char == "(":
                stack.append("(")
            elif char == ")":
                tmp = []
                while stack[-1] != "(":
                    tmp.append(stack.pop())
                stack.pop()
                if stack:
                    stack += tmp
                else:
                    res += "".join(tmp)
            elif stack:
                stack.append(char)
            else:
                res += char
        return res
