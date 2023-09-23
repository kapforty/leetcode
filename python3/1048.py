class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)

        cache = defaultdict(int)
        for word in words:
            wordLen = len(word)
            for i in range(wordLen):
                temp = word[:i] + word[i+1:]
                cache[word] = max(cache[word], 1 + cache[temp])
        
        return max(cache.values())
