class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        turns = {
            "0": ["9", "1"],
            "1": ["0", "2"],
            "2": ["1", "3"],
            "3": ["2", "4"],
            "4": ["3", "5"],
            "5": ["4", "6"],
            "6": ["5", "7"],
            "7": ["6", "8"],
            "8": ["7", "9"],
            "9": ["8", "0"]
        }
        deadends = set(deadends)
        frontier = deque([[0,"0000"]])

        # trivial case
        if "0000" in deadends:
            return -1
        
        # bfs
        while frontier:
            numTurns, curr = frontier.popleft()
            if curr == target:
                return numTurns
            for i in range(4):
                for num in turns[curr[i]]:
                    temp = curr[:i] + num + curr[i+1:]
                    if temp in deadends:
                        continue
                    deadends.add(temp)
                    frontier.append([numTurns + 1, temp])
        return -1
