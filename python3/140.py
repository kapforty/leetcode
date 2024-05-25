class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        valid = set(wordDict)
        def bt(curr, unprocessed):
            if not unprocessed:
                res.append(" ".join(curr))
                return
            for i in range(len(unprocessed)):
                if unprocessed[:i+1] in valid:
                    curr.append(unprocessed[:i+1])
                    bt(curr, unprocessed[i+1:])
                    curr.pop()
        bt([], s)
        return res
