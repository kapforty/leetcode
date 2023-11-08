class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, boxMap = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit == ".":
                    continue
                if digit in rowMap[i]:
                    return False
                if digit in colMap[j]:
                    return False
                if digit in boxMap[(i//3,j//3)]:
                    return False
                rowMap[i].add(digit)
                colMap[j].add(digit)
                boxMap[(i//3, j//3)].add(digit)
        return True

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         # rows
#         for i in range(9):
#             digits = set()
#             for j in range(9):
#                 if board[i][j] == ".":
#                     continue
#                 if board[i][j] in digits:
#                     return False
#                 digits.add(board[i][j])

#         # cols
#         for i in range(9):
#             digits = set()
#             for j in range(9):
#                 if board[j][i] == ".":
#                     continue
#                 if board[j][i] in digits:
#                     return False
#                 digits.add(board[j][i])

#         # sub-boxes
#         subBoxes = defaultdict(set)
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == ".":
#                     continue
#                 if board[i][j] in subBoxes[(i//3, j//3)]:
#                     return False
#                 subBoxes[(i//3, j//3)].add(board[i][j])

#         return True
