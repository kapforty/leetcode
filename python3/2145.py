class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        low, high = lower, upper
        for d in differences:
            low, high = max(low + d, lower), min(high + d, upper)
        return high - low + 1 if high >= low else 0
