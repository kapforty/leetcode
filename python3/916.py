class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b = defaultdict(int)
        for word in words2:
            counter = Counter(word)
            for k, v in counter.items():
                b[k] = max(b[k], v)
        
        res = []
        for word in words1:
            a = Counter(word)
            valid = True
            for k, v in b.items():
                if v > a[k]:
                    valid = False
                    break
            if valid:
                res.append(word)
        return res
