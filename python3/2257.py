class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded, guardSet, wallSet = set(), set(), set()
        for x, y in guards:
            guardSet.add((x, y))
        for x, y in walls:
            wallSet.add((x, y))
        for x, y in guardSet:
            startingX, startingY = x, y
            # left
            while y - 1 >= 0 and (x, y-1) not in guardSet and (x, y-1) not in wallSet:
                guarded.add((x, y-1))
                y -= 1
            # right
            x, y = startingX, startingY
            while y + 1 < n and (x, y+1) not in guardSet and (x, y+1) not in wallSet:
                guarded.add((x, y+1))
                y += 1
            # down
            x, y = startingX, startingY
            while x + 1 < m and (x+1, y) not in guardSet and (x+1, y) not in wallSet:
                guarded.add((x+1, y))
                x += 1
            # up
            x, y = startingX, startingY
            while x - 1 >= 0 and (x-1, y) not in guardSet and (x-1, y) not in wallSet:
                guarded.add((x-1, y))
                x -= 1
        return m*n - len(guarded) - len(guards) - len(walls)
