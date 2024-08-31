class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        charMap = defaultdict(int)
        for char in chars:
            charMap[char] += 1
        for word in words:
            counter = Counter(word)
            valid = True
            for k, v in counter.items():
                if charMap[k] < v:
                    valid = False
                    break
            if valid:
                res += len(word)
        return res        
