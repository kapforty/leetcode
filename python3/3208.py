class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors = colors + colors
        res = l = r = 0
        while r < len(colors)//2 + k - 2:
            if colors[r+1] != colors[r]:
                r += 1
            else:
                l = r = r + 1
            if r - l >= k - 1:
                res += 1
        return res
