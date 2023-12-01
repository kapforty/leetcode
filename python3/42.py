class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [(0,1)]
        res = 0
        for h in height:
            c = 1
            minHeight = min(stack[0][0], h)
            while stack and h >= stack[-1][0]:
                res += abs(minHeight - stack[-1][0]) * stack[-1][1]
                c += stack[-1][1]
                stack.pop()
            stack.append((h, c))
        return res
