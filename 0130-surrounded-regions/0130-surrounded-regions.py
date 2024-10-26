class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 0
        row,col=len(board),len(board[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False]*col for _ in range(row)]
        def BFS(r,c):
            q=deque([(r,c)])
            visited[r][c]=True
            remove=True
            ans=[]
            while q:
                #print(list(q))
                x,y=q.popleft()
                ans.append((x,y))
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        remove=False
                        continue
                    else:
                        if not visited[nx][ny] and board[nx][ny]=='O':
                            visited[nx][ny]=True
                            q.append((nx,ny))
            if remove:
                for i,j in ans:
                    board[i][j]='X'       
        def display(mat):
            for row in mat:
                print(row)
            #print('--------------')
        #display(board)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O' and not visited[i][j]:
                    BFS(i,j)
                    #print('---------BFS----------')
        return board
        