class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        flip = True
        if k < 0:
            code = code[::-1]
            k = -k
            flip = False

        code += code[:k]
        currSum = sum(code[:k])
        res = []

        for i in range(len(code) - 1 - k, -1, -1):
            res.append(currSum)
            currSum += code[i] - code[i + k]
        
        return res[::-1] if flip else res
