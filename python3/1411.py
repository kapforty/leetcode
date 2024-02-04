class Solution:
    def numOfWays(self, n: int) -> int:
        # two colors: 121 131 212 232 313 323
        # three colors: 123 132 213 231 312 321
        twoColors, threeColors = 6, 6
        for i in range(1, n):
            twoColors, threeColors = 3 * twoColors + 2 * threeColors, 2 * twoColors + 2 * threeColors
        return (twoColors + threeColors) % (10**9 + 7)