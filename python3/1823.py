class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        game = deque([i for i in range(1, n+1)])
        while len(game) > 1:
            for i in range(k-1):
                game.append(game.popleft())
            game.popleft()
        return game[0]
