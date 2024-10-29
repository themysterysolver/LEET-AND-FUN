class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def display(mat):
            for row in board:
                print(row)
            print('-----------------')
        directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        row,col=len(board),len(board[0])
        def checker(r,c):
            count=0
            for dx,dy in directions:
                nx,ny=r+dx,c+dy
                if nx<0 or ny<0 or nx>=row or ny>=col or board[nx][ny]==0:
                    continue
                elif board[nx][ny]==1:
                    count+=1
            if board[r][c]==1:
                if count<2 or  count>3:
                    return 0
                elif count in [2,3]:
                    return 1
            else:
                if count==3:
                    return 1
                else:
                    return 0
        result=[row[:] for row in board]
        for i in range(row):
            for j in range(col):
                print('i j b c')
                print(i,j,board[i][j],checker(i,j))
                result[i][j]=checker(i,j)
                display(result)
        for i in range(row):
            for j in range(col):
                board[i][j]=result[i][j]
        