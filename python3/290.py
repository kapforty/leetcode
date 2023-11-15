class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = defaultdict(str)
        words = s.split(" ")

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        
        for i in range(len(pattern)):
            hashMap[pattern[i]] = words[i]

        res = []
        for char in pattern:
            res.append(hashMap[char])

        return res == words
