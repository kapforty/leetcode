class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# class Trie:

#     def __init__(self):
#         self.trie = set()
#         self.prefix = set()

#     def insert(self, word: str) -> None:
#         for i in range(1, len(word) + 1):
#             self.prefix.add(word[0:i])
#         self.trie.add(word)

#     def search(self, word: str) -> bool:
#         return word in self.trie

#     def startsWith(self, prefix: str) -> bool:
#         return prefix in self.prefix


