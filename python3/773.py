class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # define target state
        target = (1,2,3,4,5,0)

        # define valid slides
        slides = {0: [1,3], 1: [0,2,4], 2: [1,5], 3: [0,4], 4: [1,3,5], 5: [2, 4]}

        # convert board to 6-tuple
        board = (board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2])

        # bfs
        seen = {board}
        d = deque([(board, 0, board.index(0))])
        while d:
            state, moves, pos = d.popleft()
            if state == target:
                return moves
            for slide in slides[pos]:
                temp = list(state)
                temp[pos], temp[slide] = temp[slide], temp[pos]
                temp = tuple(temp)
                if temp not in seen:
                    d.append((temp, moves + 1, slide))
                    seen.add(temp)
        return -1
