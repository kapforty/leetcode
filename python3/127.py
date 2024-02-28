class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # helper function to determine valid transformations
        def validTransformation(word1, word2):
            if word1 == word2:
                return False
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
                    if count > 1:
                        return False
            return True

        # bfs
        res = 0
        visited = {beginWord}
        frontier = [beginWord]
        while frontier:
            res += 1
            temp = []
            for word1 in frontier:
                if word1 == endWord:
                    return res
                for word2 in wordList:
                    if word2 not in visited and validTransformation(word1, word2):
                        temp.append(word2)
                        visited.add(word2)
            frontier = temp
        
        return 0

