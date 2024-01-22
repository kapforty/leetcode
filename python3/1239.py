class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        def bt(chars, arr):
            nonlocal res
            res = max(res, len(chars))
            if not arr:
                return
            bt(chars, arr[1:])
            temp = chars + arr[0]
            if len(temp) == len(set(temp)):
                bt(temp, arr[1:])
        bt("", arr)
        return res
            