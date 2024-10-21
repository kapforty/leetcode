class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        def bt(used, substr):
            nonlocal res
            res = max(res, len(used))
            for i in range(len(substr)):
                l, r = substr[:i+1], substr[i+1:]
                if l in used or r in used: continue
                used.add(l)
                bt(used, r)
                used.remove(l)
        bt(set(), s)
        return res
