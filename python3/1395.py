class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating)-1):
            smallerLeft = smallerRight = biggerLeft = biggerRight = 0
            curr = rating[i]
            for j in range(0, i):
                if rating[j] < curr:
                    smallerLeft += 1
                else:
                    biggerLeft += 1
            for k in range(i+1, len(rating)):
                if rating[k] < curr:
                    smallerRight += 1
                else:
                    biggerRight += 1
            res += smallerLeft * biggerRight + biggerLeft * smallerRight
        return res
