class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]

        res = set()
        words = set(words)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # backtrack
        def bt(r, c, visited, curr, trie):
            if curr in words:
                res.add(curr)
            for x, y in directions:
                if (r+x, c+y) in visited or r+x < 0 or r+x >= len(board) or c+y < 0 or c+y >= len(board[0]) or board[r+x][c+y] not in trie:
                    continue
                visited.add((r+x, c+y))
                bt(r+x, c+y, visited, curr + board[r+x][c+y], trie[board[r+x][c+y]])
                visited.remove((r+x, c+y))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] not in trie:
                    continue
                bt(r, c, {(r,c)}, board[r][c], trie[board[r][c]])
        
        return list(res)
