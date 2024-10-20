class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c in "tf":
                stack.append(c == "t")
            elif c in "!&|":
                stack.append(c)
            elif c == ")":
                bools = []
                while stack and type(stack[-1]) == bool:
                    bools.append(stack.pop())
                match stack.pop():
                    case "!": res = not bools[0]
                    case "&": res = all(bools)
                    case _: res = any(bools)
                stack.append(res)
        return stack[0]
