class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [1]

        for char in s[1:]:
            if stack[-1] >= k:
                break
            if char.isnumeric():
                stack.append(stack[-1] * int(char))
            else:
                stack.append(stack[-1] + 1)

        for idx, val in reversed(list(enumerate(stack))):
            k %= val
            if k == 0 and s[idx].isalpha():
                return s[idx]
