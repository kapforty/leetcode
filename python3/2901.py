class Solution:
    def hasHammingDistanceOfOne(self, word1, word2):
        if len(word1) != len(word2):
            return False
        distance = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                distance += 1
        return distance == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [] # (word, group, length, prev)
        for i, word in enumerate(words):
            length, prev = 1, None
            for j in range(len(dp)):
                w, g, l, p = dp[j]
                if g != groups[i] and l >= length and self.hasHammingDistanceOfOne(w, word):
                    length, prev = l + 1, j
            dp.append((word, groups[i], length, prev))

        res, curr = [], max(dp, key=lambda x: x[2])
        while curr:
            res.append(curr[0])
            if curr[3] is None:
                break
            curr = dp[curr[3]]
        return res[::-1]
