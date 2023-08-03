class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(word, x, y, prevDirection, visited):
            nonlocal res
            if word == "":
                res = True
                return
            if (x,y) in visited:
                return
            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return
            if word[0] != board[y][x]:
                return
            else:
                for direction in directions:
                    if (-prevDirection[0], -prevDirection[1]) != direction:
                        visited.add((x, y))
                        dfs(word[1:], x+direction[0], y+direction[1], direction, visited.copy())

        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for y in range(len(board)):
            for x in range(len(board[0])):
                visited = set()
                dfs(word, x, y, (0,0), visited)
                if res:
                    return res

        return res
