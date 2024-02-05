class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # convert board into 1d array
        board = board[::-1]
        for i in range(1, len(board), 2):
            board[i] = board[i][::-1]
        board = sum(board, [])

        # adjust board for zero-based indexing
        for i in range(len(board)):
            if board[i] != -1:
                board[i] -= 1

        # bfs
        frontier = deque()
        frontier.append([0, 0])
        visited = {0}
        while frontier:
            curr, steps = frontier.popleft()
            for i in range(1, 7):
                nxt = curr + i
                if nxt >= len(board):
                    break
                if board[nxt] != -1:
                    nxt = board[nxt]
                if nxt == len(board) - 1:
                    return steps + 1
                if nxt not in visited:
                    frontier.append([nxt, steps + 1])
                    visited.add(nxt)
        return -1
