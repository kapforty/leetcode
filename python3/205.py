class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zippedSet = set(zip(s, t))
        return len(zippedSet) == len(set(s)) == len(set(t))
