class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        chars = Counter(s)
        stack = []
        stackSet = set()

        for char in s:
            chars[char] -= 1
            if char in stackSet:
                continue
            while stack and chars[stack[-1]] > 0 and stack[-1] > char:
                stackSet.remove(stack.pop())
            stack.append(char)
            stackSet.add(char)
        return "".join(stack)
