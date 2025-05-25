class Solution:
        def longestPalindrome(self, words: List[str]) -> int:
            pairs, sym, nonPaired = 0, 0, Counter()
            for w in words:
                if nonPaired[w[:: -1]] > 0:
                    pairs += 1
                    nonPaired[w[:: -1]] -= 1
                    sym -= 1 if w[0] == w[1] else 0
                else:
                    nonPaired[w] += 1    
                    sym += 1 if w[0] == w[1] else 0
            return pairs * 4 + (2 if sym > 0 else 0)
