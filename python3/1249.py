class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        badIdx = set()
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(("(", i))
            elif s[i] == ")" and stack:
                stack.pop()
            elif s[i] == ")" and not stack:
                badIdx.add(i)
        while stack:
            badIdx.add(stack.pop()[1])
        
        res = ""
        for i in range(len(s)):
            if i in badIdx:
                continue
            res += s[i]
        return res
