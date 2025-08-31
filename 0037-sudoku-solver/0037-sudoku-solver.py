class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        def dis(msg,mat):
            print(msg)
            for idx,r in enumerate(mat):
                print(idx,r)
            print('----------------')
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3)*3+j//3].add(board[i][j])
        #print(f"{row}\n{col}\n{box}")
        #dis("row",row)
        #dis("col",col)
        #dis("box",box)
        def backtrack(r,c):
            if r == 9:
                return True
            elif c == 9:
                return backtrack(r+1,0)
            else:
                idx = (r//3)*3+c//3
                if board[r][c]==".":
                    for j in range(1,10):
                        s = str(j)
                        if s not in row[r] and s not in col[c] and s not in box[idx]:
                            board[r][c] = s
                            row[r].add(s)
                            col[c].add(s)
                            box[idx].add(s)
                        
                            if backtrack(r,c+1):
                                return True
                            board[r][c] = "."
                            row[r].remove(s)
                            col[c].remove(s)
                            box[idx].remove(s)
                else:
                    return backtrack(r,c+1)
                return False
        backtrack(0,0)
        return board


                    