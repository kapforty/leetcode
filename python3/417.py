class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        pacSet, atlSet = set(), set()

        def dfs(r, c, currVal, ocean):
            ocean.add((r,c))

            for direction in directions:
                row, col = r + direction[0], c + direction[1]
                if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
                    continue
                if (row, col) in ocean:
                    continue
                if heights[row][col] >= heights[r][c]:
                    dfs(row, col, heights[row][col], ocean)
        
        for r in range(len(heights)):
            dfs(r, 0, heights[r][0], pacSet)
            dfs(r, COLS-1, heights[r][COLS-1], atlSet)
        for c in range(len(heights[0])):
            dfs(0, c, heights[0][c], pacSet)
            dfs(ROWS-1, c, heights[ROWS-1][c], atlSet)

        res = []
        for (r, c) in pacSet & atlSet:
            res.append([r, c])
        return res
