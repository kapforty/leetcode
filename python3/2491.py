class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # calculate target skill of each team
        target = 2 * sum(skill) / len(skill)
        if target != floor(target):
            return -1

        # divide players
        res = 0
        players = defaultdict(int)
        for player in skill:
            find = target - player
            if find in players:
                players[find] -= 1
                if players[find] == 0:
                    del players[find]        
                res += find * player
            else:
                players[player] += 1
        return floor(res) if not players else -1
