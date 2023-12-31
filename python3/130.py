class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        marked = set()

        def dfs(row, col):
            if (row, col) in visited or row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == "X":
                return
            visited.add((row, col))
            if board[row][col] == "O":
                marked.add((row, col))
            for direction in directions:
                dfs(row + direction[0], col + direction[1])

        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS-1, i)
        for i in range(1, ROWS-1):
            dfs(i, 0)
            dfs(i, COLS-1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in marked:
                    board[i][j] = "X"
        return board
