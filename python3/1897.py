class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charMap = defaultdict(int)
        for word in words:
            for char in word:
                charMap[char] += 1
        
        for v in charMap.values():
            if v % len(words) != 0:
                return False
        
        return True
