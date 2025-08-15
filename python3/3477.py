class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res, used = 0, set()
        for fruit in fruits:
            placed = False
            for i, basket in enumerate(baskets):
                if i not in used and basket >= fruit:
                    placed = True
                    used.add(i)
                    break
            if not placed:
                res += 1
        return res
