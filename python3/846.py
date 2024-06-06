class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # trivial case
        if groupSize == 1:
            return True

        # keep track of current group sizes ending with specific card (key)
        hands = defaultdict(list)
        hand.sort()
        for card in hand:
            if len(hands[card - 1]) == 0:
                hands[card].append(1)
            else:
                popped = hands[card - 1].pop()
                if popped + 1 != groupSize:
                    hands[card].append(popped + 1)

        # check for any partially filled groups
        for v in hands.values():
            if len(v) > 0 :
                return False
        return True
