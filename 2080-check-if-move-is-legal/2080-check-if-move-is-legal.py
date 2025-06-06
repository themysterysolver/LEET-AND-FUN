class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def display(mat):
            for row in mat:
                print(row)
            print('---------')
        display(board)

        r,c=rMove,cMove
        row,col=len(board),len(board[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        for dx,dy in directions:
            i,j=r+dx,c+dy 
            size=2
            while row>i>=0<=j<col:
                if board[i][j]=="." or (size<3 and board[i][j]==color):
                    break
                if board[i][j]==color:
                    return True
                i+=dx
                j+=dy
                size+=1
        return False