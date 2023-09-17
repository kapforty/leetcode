class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelSet = {'a','e','i','o','u'}
        res = 0
        currCount = 0

        for char in s[:k]:
            if char in vowelSet:
                currCount += 1

        res = max(res, currCount)

        for i in range(k, len(s), 1):
            if s[i-k] in vowelSet:
                currCount -= 1
            if s[i] in vowelSet:
                currCount += 1
            res = max(res, currCount)

        return res
