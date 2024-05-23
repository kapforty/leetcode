class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letterMap = Counter(letters)
        charMaps, scores = [], []
        for word in words:
            charMap = defaultdict(int)
            currScore = 0
            valid = True
            for char in word:
                charMap[char] += 1
                currScore += score[ord(char) - ord("a")]
            for k, v in charMap.items():
                if v > letterMap[k]:
                    valid = False
                    break
            if valid:
                charMaps.append(charMap)
                scores.append(currScore)

        res = 0
        def bt(currScore, currMap, maps, scores):
            nonlocal res
            res = max(res, currScore)
            for i in range(len(maps)):
                temp = currMap.copy()
                for k, v in maps[i].items():
                    temp[k] += v
                valid = True
                for k, v in temp.items():
                    if v > letterMap[k]:
                        valid = False
                        break
                if valid:
                    bt(currScore + scores[i], temp, maps[i+1:], scores[i+1:])
        
        bt(0, defaultdict(int), charMaps, scores)
        return res
