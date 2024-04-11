class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # monotonic stack (increasing)
        for val in num:
            while k > 0 and stack and stack[-1] > val:
                stack.pop()
                k -= 1
            stack.append(val)
        
        # remove excess digits
        if k > 0:
            stack = stack[:-k]

        # remove leading zeroes
        res = "".join(stack).lstrip("0")
        
        # return result, check if string is empty
        return res if res else "0"
