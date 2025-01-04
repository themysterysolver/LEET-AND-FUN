class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def display(matrix):
            for row in matrix:
                print(row)
            print('----------------------')
        row,col=len(mat),len(mat[0])
        result=[[0]*col for _ in range(row)]
        q=deque([])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    q.append((i,j))
                    visited[i][j]=True
        #print(q)
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            x,y=q.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col or visited[nx][ny]:
                    continue
                if mat[nx][ny]==1 and result[nx][ny]<=result[x][y]:
                    result[nx][ny]=result[x][y]+1
                    q.append((nx,ny))
                    visited[nx][ny]=True
        #display(result)
        return result