class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = t = 0
        while s < len(start) and t < len(start):
            if start[s] == "_":
                s += 1
                continue
            if target[t] == "_":
                t += 1
                continue
            if start[s] != target[t]:
                return False
            if start[s] == "L" and s < t:
                return False
            if start[s] == "R" and s > t:
                return False
            s += 1
            t += 1
        
        while s < len(start):
            if start[s] != "_":
                return False
            s += 1
        while t < len(target):
            if target[t] != "_":
                return False
            t += 1
        
        return True
