class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strings = []
        for num in nums:
            strings.append(str(num))
        strings.sort(key=lambda x: x*10, reverse=True)
        if strings[0] == "0": return "0"
        return "".join(strings)
