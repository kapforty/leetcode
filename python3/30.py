class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        wordMap = defaultdict(int)
        
        # initialize values in wordMap
        for word in words:
            wordMap[word] += 1
        
        # iterate through windows, split each window into <len(words[0])> words
        l, r = 0, len(words) * len(words[0])
        while r <= len(s):
            curr, currMap = s[l:r], defaultdict(int)
            for i in range(l, r, len(words[0])):
                currWord = s[i:i + len(words[0])]
                currMap[currWord] += 1
            if currMap == wordMap:
                res.append(l)
            l += 1
            r += 1
        
        return res
