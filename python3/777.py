class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if Counter(start) != Counter(end):
            return False
            
        startStack, endStack = [], []
        for i, char in enumerate(start):
            if char != "X":
                startStack.append((char, i))
        for i, char in enumerate(end):
            if char != "X":
                endStack.append((char, i))

        for i in range(len(startStack)):
            if startStack[i][0] != endStack[i][0]:
                return False
            if startStack[i][0] == "R" and startStack[i][1] > endStack[i][1]:
                return False
            if startStack[i][0] == "L" and startStack[i][1] < endStack[i][1]:
                return False
        
        return True
