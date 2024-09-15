class Solution:
    def validSudoko(self,board):
        row_hash=[set() for _ in range(len(board))]
        col_hash=[set() for _ in range(len(board))]
        box_hash=[set() for _ in range(len(board))]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                box_index=(i//3)*3+j//3
                if num is not ".":
                    if num in row_hash[i] or num in col_hash[j] or num in box_hash[box_index]:
                        return False
                    row_hash[i].add(num)
                    col_hash[j].add(num)
                    box_hash[box_index].add(num)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validSudoko(board)
        