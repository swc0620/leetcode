class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element != ".":
                    res.extend([(i, element), (element, j), (i // 3, j // 3, element)])
        return len(res) == len(set(res))

        # # check rows
        # for row in board:
        #     check = set()
        #     for c in row:
        #         if c == ".":
        #             continue
        #         if c in check:
        #             return False
        #         check.add(c)
        
        # # check columns
        # for j in range(9):
        #     check = set()
        #     for i in range(9):
        #         if board[i][j] == ".":
        #             continue
        #         if board[i][j] in check:
        #             return False
        #         check.add(board[i][j])
        
        # # check sub-box
        # for x in range(3):
        #     for y in range(3):
        #         check = set()
        #         for i in range(3):
        #             for j in range(3):
        #                 if board[3*x+i][3*y+j] == ".":
        #                     continue
        #                 if board[3*x+i][3*y+j] in check:
        #                     return False
        #                 check.add(board[3*x+i][3*y+j])
        
        # return True
