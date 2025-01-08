class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for j in range(1, len(words)):
            for i in range(j):
                if len(words[i]) > len(words[j]):
                    continue
                if words[j][:len(words[i])] == words[j][-len(words[i]):] == words[i]:
                    res += 1
        return res
