class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = k = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack = stack + list(int(k) * temp)
        
        return "".join(stack)
