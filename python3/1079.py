class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res, charMap = -1, Counter(tiles)
        def bt():
            nonlocal res
            res += 1
            for char, count in charMap.items():
                if count > 0:
                    charMap[char] -= 1
                    bt()
                    charMap[char] += 1
        bt()
        return res
