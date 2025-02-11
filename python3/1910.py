class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack, length, part = [], len(part), list(part)
        for c in s:
            stack.append(c)
            while len(stack) >= length and stack[len(stack) - length:] == part:
                stack = stack[:-length]
        return "".join(stack)
