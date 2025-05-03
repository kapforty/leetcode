class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # validate dominos
        valid = set([tops[0], bottoms[0]])
        for i in range(1, len(tops)):
            valid &= set([tops[i], bottoms[i]])
            if not valid:
                return -1
        valid = list(valid)[0]
        
        # calculate result
        return min(len(tops) - tops.count(valid), len(tops) - bottoms.count(valid))
