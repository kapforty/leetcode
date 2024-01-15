class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lossHistory = defaultdict(int)

        for match in matches:
            players.add(match[0])
            players.add(match[1])
            lossHistory[match[1]] += 1
        
        zero, one = [], []
        for player in players:
            if lossHistory[player] == 0:
                zero.append(player)
            if lossHistory[player] == 1:
                one.append(player)
        
        zero.sort()
        one.sort()

        return [zero, one]
