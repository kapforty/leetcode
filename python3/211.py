class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not char in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def helper(currNode, currWord):
            if len(currWord) == 0 and currNode.isWord:
                return True
            if len(currWord) == 0:
                return False
            if currWord[0] == ".":
                for child in currNode.children.values():
                    if helper(child, currWord[1:]):
                        return True
                return False
            elif currWord[0] in currNode.children:
                return helper(currNode.children[currWord[0]], currWord[1:])
            else:
                return False
                
        return helper(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
