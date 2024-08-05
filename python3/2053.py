class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        for char in arr:
            if counter[char] == 1:
                k -= 1
                if k == 0:
                    return char
        return ""
