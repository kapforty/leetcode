class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live = set()
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                liveNeighbors = 0
                for direction in directions:
                    if i + direction[0] < 0 or i + direction[0] >= len(board) or j + direction[1] < 0 or j + direction[1] >= len(board[0]):
                        continue
                    if board[i + direction[0]][j + direction[1]] == 1:
                        liveNeighbors += 1
                if board[i][j] == 0 and liveNeighbors == 3:
                    live.add((i,j))
                elif board[i][j] == 1 and liveNeighbors == 2 or liveNeighbors == 3:
                    live.add((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) in live:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
