class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = 0

        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i-1] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    count += 1
                else:
                    count -= 1

        return count > 0
