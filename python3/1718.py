class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res, used = [0 for _ in range(2*n - 1)], set()
        def bt(i):
            if i == len(res):
                return True
            for num in reversed(range(1, n + 1)):
                if num in used or (num > 1 and (i + num >= len(res) or res[i + num])):
                    continue
                used.add(num)
                res[i] = num
                if num > 1:
                    res[i + num] = num
                j = i
                while j < len(res) and res[j]:
                    j += 1
                if bt(j):
                    return True
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i + num] = 0
            return False
        bt(0)
        return res
