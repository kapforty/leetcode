class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [i for i in range(26)]

        # union by rank
        def union(c1, c2):
            c1, c2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            p1, p2 = find(c1), find(c2)
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        # find w/ path compression
        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]

        # run union by rank w/ path compression
        for i in range(len(s1)):
            union(s1[i], s2[i])

        # build result
        res = ""
        for c in baseStr:
            res += chr(find(ord(c) - ord('a')) + ord('a'))
        return res
