class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        oddCount = 0
        for key, v in counter.items():
            if v % 2 != 0:
                oddCount += 1
        return oddCount <= k <= len(s)
