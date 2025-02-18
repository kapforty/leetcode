class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, used = [0] * (len(pattern) + 1), set()
        def bt(i, low, high):
            for n in range(low + 1, high):
                if n in used or n <= low or n >= high:
                    continue
                res[i] = n
                used.add(n)
                if i == len(pattern):
                    return True
                elif pattern[i] == "I" and bt(i + 1, n, 10):
                    return True
                elif bt(i + 1, 0, n):
                    return True
                res[i] = 0
                used.remove(n)
            return False
        bt(0, 0, 10)
        return "".join([str(n) for n in res])
