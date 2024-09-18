class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row,col=len(board),len(board[0])
        visited=[[False]*col for _ in range(row)]
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def BFS(r,c):
            q=deque([(r,c)])
            visited[r][c]=True
            while q:
                x,y=q.popleft()
                for dx,dy in direction:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx==row or ny==col or board[nx][ny]=='.':
                        continue
                    elif board[nx][ny]=='X' and not visited[nx][ny]:
                        visited[nx][ny]=True
                        q.append((nx,ny))
        
        count=0
        for i in range(row):
            for j in range(col):
                if board[i][j]=='X' and not visited[i][j]:
                    BFS(i,j)
                    count+=1
        return count
        