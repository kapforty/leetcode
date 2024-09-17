class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = Counter(s1.split(" ")), Counter(s2.split(" "))
        res = []
        for k, v in s1.items():
            if v == 1 and k not in s2:
                res.append(k)
        for k, v in s2.items():
            if v == 1 and k not in s1:
                res.append(k)
        return res
