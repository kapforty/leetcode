class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x:(x[0], -x[1]))
        maxi = properties[-1][-1]
        res = 0
        while properties:
            curr = properties.pop()
            if curr[-1] < maxi:
                res += 1 
            maxi = max(maxi, curr[-1])
        return res
