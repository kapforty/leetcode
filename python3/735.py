class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for roid in asteroids:
            if roid > 0 or not stack:
                stack.append(roid)
                continue
            while stack and stack[-1] > 0 and stack[-1] < abs(roid):
                stack.pop()
            if not stack:
                stack.append(roid)
            elif stack[-1] < 0:
                stack.append(roid)
            elif stack and stack[-1] > 0 and stack[-1] == abs(roid):
                stack.pop()

        return stack      
