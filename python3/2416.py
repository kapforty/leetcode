class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # compute prefix tree from words
        trie = TrieNode()
        for word in words:
            curr = trie
            for char in word:
                if not curr.child[ord(char) - ord('a')]:
                    curr.child[ord(char) - ord('a')] = TrieNode()
                curr = curr.child[ord(char) - ord('a')]
                curr.count += 1
        
        # calculate scores
        res = []
        for word in words:
            curr = trie
            score = 0
            for char in word:
                curr = curr.child[ord(char) - ord('a')]
                score += curr.count
            res.append(score)
        return res
