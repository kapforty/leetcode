class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        frontier, visited = [entrance], {tuple(entrance)}
        res = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        while frontier:
            res += 1
            for i in range(len(frontier)):
                r, c = frontier.pop(0)
                for u, v in directions:
                    if (r + u, c + v) not in visited:
                        if r + u < 0 or c + v < 0 or r + u >= ROWS or c + v >= COLS or maze[r + u][c + v] == "+":
                            continue
                        if r + u == 0 or c + v == 0 or r + u == ROWS - 1 or c + v == COLS - 1:
                            return res
                        frontier.append([r + u, c + v])
                        visited.add((r + u, c + v))
        return -1
