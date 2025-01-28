class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        count=0
        visited=[[False]*col for _ in range(row)]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def BFS(r,c):
            visited[r][c]=True
            q=deque([(r,c)])
            fish=0
            while q:
                x,y=q.popleft()
                fish+=grid[x][y]
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col or visited[nx][ny]:
                        continue
                    else:
                        if grid[nx][ny]>0:
                            #fish+=grid[nx][ny]
                            q.append((nx,ny))
                            visited[nx][ny]=True
            #print(i,j,fish)
            #print('------------------------')
            return fish
        for i in range(row):
            for j in range(col):
                if grid[i][j]>0 and not visited[i][j]:
                    count=max(count,BFS(i,j))
                    #print(i,j,count)
        return count