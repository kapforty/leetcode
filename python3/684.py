class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [i for i in range(len(edges) + 1)]
        r = [1 for i in range(len(p))]

        def find(n):
            if n != p[n]:
                p[n] = find(p[n])
            return p[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if r[p1] > r[p2]:
                p[p2] = p1
                r[p1] += r[p2]
            else:
                p[p1] = p2
                r[p2] += r[p1]
            return True

        for e in edges:
            if not union(e[0], e[1]):
                return e
