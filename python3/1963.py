class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and char == "]" and stack[-1] == "[":
                stack.pop()
                continue
            stack.append(char)
            
        res = len(stack) // 4
        if len(stack) % 4 != 0:
            res += 1
        return res
