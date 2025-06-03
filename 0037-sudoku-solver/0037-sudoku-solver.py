class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3)*3+j//3].add(board[i][j])
        def backtrack(i,j):
            if i==9:
                return True
            if j==9:
                return backtrack(i+1,0)
            if board[i][j]!=".":
                return backtrack(i,j+1)
            if board[i][j]==".":
                for n in map(str,range(1,10)):
                    bidx=(i//3)*3+j//3
                    if n in row[i] or n in col[j] or n in box[bidx]:
                        continue
                    else:
                        row[i].add(n)
                        col[j].add(n)
                        box[bidx].add(n)
                        board[i][j]=n
                        if backtrack(i,j+1):
                            return True
                        board[i][j]="."
                        row[i].remove(n)
                        col[j].remove(n)
                        box[bidx].remove(n)
                return False
        backtrack(0,0)
        return board

                    