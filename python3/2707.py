class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False
    def calculate(trie, s: str):
        indices = []
        curr = trie
        idx = -1
        for char in s:
            if not curr.child[ord(char) - ord('a')]:
                return indices
            curr = curr.child[ord(char) - ord('a')]
            idx += 1
            if curr.wordEnd:
                indices.append(idx)
        return indices

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # turn dictionary for words into trie
        trie = TrieNode()
        for word in dictionary:
            curr = trie
            for char in word:
                if not curr.child[ord(char) - ord('a')]:
                    curr.child[ord(char) - ord('a')] = TrieNode()
                curr = curr.child[ord(char) - ord('a')]
            curr.wordEnd = True

        # dp
        dp = [i for i in range(len(s) + 1)]
        dictionary = set(dictionary)
        for i, char in enumerate(s):
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            indices = trie.calculate(s[i:])
            for idx in indices:
                dp[i+idx+1] = min(dp[i+idx+1], dp[i])
        return dp[-1]
