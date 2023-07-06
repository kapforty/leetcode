class Solution:
    def isValid(self, s: str) -> bool:
        pMap = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in pMap:
                if not stack:
                    return False
                if stack.pop() != pMap[c]:
                    return False
            else:
                stack.append(c)
        return False if stack else True
