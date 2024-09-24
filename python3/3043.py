class TrieNode:
    def __init__(self):
        self.child = [None] * 10
    def calculate(trie, s: str):
        length = 0
        for char in s:
            if not trie.child[ord(char) - 48]:
                break
            length += 1
            trie = trie.child[ord(char) - 48]
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # convert longer array into a trie
        if len(arr2) > len(arr1):
            arr1, arr2 = arr2, arr1
        trie = TrieNode()
        for num in arr1:
            num = str(num)
            curr = trie
            for char in num:
                if not curr.child[ord(char) - 48]:
                    curr.child[ord(char) - 48] = TrieNode()
                curr = curr.child[ord(char) - 48]
        
        # calculate longest common prefix
        res = 0
        for num in arr2:
            res = max(res, trie.calculate(str(num)))
        return res
