class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def minesweeper(r,c):
            row,col=len(board),len(board[0])
            directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
            q=deque([(r,c)])
            visited=[[False]*col for _ in range(row)]
            visited[r][c]=True
            def find(r,c):
                count=0
                for dx,dy in directions:
                    nx,ny=r+dx,c+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        continue
                    print('[nx][ny]',nx,ny,board[nx][ny])
                    if board[nx][ny]=='M':
                        print('found')
                        count+=1
                        print('count',count)
                return count
            co=find(r,c)
            if co>0:
                board[r][c]=str(co)
                return
            while q:
                l=len(q)
                for i in range(l):
                    x,y=q.popleft()
                    count=find(x,y)
                    if count>0:
                        board[x][y]=str(count)
                    else:
                        board[x][y]='B'
                        for dx,dy in directions:
                            nx,ny=x+dx,y+dy
                            if nx<0 or ny<0 or nx>=row or ny>=col:
                                continue
                            if not visited[nx][ny]:
                                q.append((nx,ny))
                                visited[nx][ny]=True
        def display(mat):
            for row in mat:
                print(row)
            print('---------------------------')
        display(board)
        print('That point:',click[0],click[1],':',board[click[0]][click[1]])
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            display(board)
            return board
        if board[click[0]][click[1]]=='E':
            minesweeper(click[0],click[1])
        display(board)
        return board