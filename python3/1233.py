class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        folder.sort()
        trie = TrieNode()
        for path in folder:
            f = path.split("/")[1:]
            curr, valid = trie, True
            for c in f:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                if curr.end:
                    valid = False
                    break
            if valid:
                curr.end = True
                res.append(path)
        return res
