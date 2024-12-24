class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def display(matrix):
            for row in matrix:
                print(row)
            print('-------------')
        display(grid)
        def convertToThreeCrossThree(grid):
            n=len(grid)
            matrix=[[0]*(n*3) for i in range(n*3)]
            display(matrix)
            for i in range(n):
                for j in range(n):
                    baser,basec=i*3,j*3
                    if grid[i][j]=='/':
                        matrix[baser][basec+2]=matrix[baser+1][basec+1]=matrix[baser+2][basec]=1
                    elif grid[i][j]=='\\':
                        matrix[baser][basec]=matrix[baser+1][basec+1]=matrix[baser+2][basec+2]=1
            return matrix 
        grid=convertToThreeCrossThree(grid)
        display(grid)
        #flood fill algo
        visited=[[False]*len(grid) for _ in range(len(grid))]
        row=col=len(grid)
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def BFS(r,c):
            q=deque([(r,c)])
            visited[r][c]=True
            while q:
                x,y=q.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=len(grid) or ny>=len(grid):
                        continue
                    else:
                        if not visited[nx][ny] and grid[nx][ny]==0:
                            q.append((nx,ny))
                            visited[nx][ny]=True
        count=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]==0 and not visited[i][j]:
                    BFS(i,j)
                    count+=1
        return count