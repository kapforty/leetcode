class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box[0]), len(box)
        res = [["" for _ in range(COLS)] for _ in range(ROWS)]
        
        for c, row in enumerate(box):
            stack = []
            for cell in row[::-1]:
                fill = 0
                while cell == "#" and stack and stack[-1] == ".":
                    stack.pop()
                    fill += 1
                stack.append(cell)
                for _ in range(fill):
                    stack.append(".")
            while len(stack) < ROWS:
                stack.append(".")
            for r, cell in enumerate(stack):
                res[ROWS-1-r][COLS-1-c] = cell
        return res
