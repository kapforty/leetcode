# funky one liner
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(0 if not left else max(left), 0 if not right else n - min(right))

# same solution as above, more readable
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l = 0 if not left else max(left)
        r = 0 if not right else n - min(right)
        return max(l, r)
