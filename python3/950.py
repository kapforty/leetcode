class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = deque()
        deck.sort()
        res.append(deck.pop())
        while deck:
            res.appendleft(res.pop())
            res.appendleft(deck.pop())
        return res
