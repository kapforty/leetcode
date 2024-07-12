class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        substr = ["a", "b"] if x > y else ["b", "a"]
        stack = []
        res = 0
        for char in s:
            stack.append(char)
            while len(stack) > 1 and stack[-2:] == substr:
                res += max(x, y)
                stack.pop()
                stack.pop()
        
        substr[0], substr[1] = substr[1], substr[0]
        s = "".join(stack)
        stack = []
        for char in s:
            stack.append(char)
            while len(stack) > 1 and stack[-2:] == substr:
                res += min(x, y)
                stack.pop()
                stack.pop()
        
        return res
