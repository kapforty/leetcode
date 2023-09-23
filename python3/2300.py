class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        numPotions = len(potions)
        potions.sort()
        res = []

        for spell in spells:
            l, r = 0, numPotions
            while l < r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
            res.append(numPotions - l)

        return res
