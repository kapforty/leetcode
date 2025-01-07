class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i].find(words[j]) > -1:
                    res.add(words[j])
        return list(res)
