class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        def DFS(r,c,i):
            if r<0 or c<0 or r>=row or c>=col or board[r][c]!=word[i]:
                return False
            if i==len(word)-1:
                if word[i]==board[r][c]:
                    return True
                else:
                    return False
            temp,board[r][c]=board[r][c],'#'
            found=(DFS(r,c+1,i+1) or DFS(r+1,c,i+1) or DFS(r-1,c,i+1) or DFS(r,c-1,i+1))
            board[r][c]=temp
            return found
        def display(thing):
            for row in thing:
                print(row)
            print('---------------------')
        display(board)
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if len(word)==1 or DFS(i,j,0):
                        return True
        return False