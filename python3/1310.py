class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        left, right = [arr[0]], deque([arr[-1]])
        for val in arr[1:]:
            left.append(left[-1] ^ val)
        for val in arr[-2::-1]:
            right.appendleft(right[0] ^ val)
        
        res = []
        for x, y in queries:
            curr = left[-1]
            if x > 0:
                curr ^= left[x - 1]
            if y < len(arr) - 1:
                curr ^= right[y + 1]
            res.append(curr)
        return res
