# recursive approach
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(arr, curr):
            nonlocal res
            if len(arr) == k:
                res.append(arr)
                return
            for i in range(curr+1, n+1):
                backtrack(arr + [i], i)
            
        backtrack([], 0)

        return res

# iterative approach
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[i] for i in range(1, n+1)]

        while len(res[0]) < k:
            temp = []
            for arr in res:
                for i in range(1, n+1):
                    if i > arr[-1]:
                        temp.append(arr + [i])
            res = temp

        return res
