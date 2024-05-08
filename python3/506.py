class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreSorted = sorted(score, reverse=True)
        scoreToRank = defaultdict(str)

        for i, s in enumerate(scoreSorted):
            if i > 2:
                scoreToRank[s] = str(i + 1)
            elif i == 2:
                scoreToRank[s] = "Bronze Medal"
            elif i == 1:
                scoreToRank[s] = "Silver Medal"
            else:
                scoreToRank[s] = "Gold Medal"

        for i in range(len(score)):
            score[i] = scoreToRank[score[i]]
        
        return score
