class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        obstacle=[[float('inf')]*col for _ in range(row)]
        q=deque([(0,0,0)])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        obstacle[0][0]=0
        while q:
            obs,x,y=q.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col:
                    continue
                if obstacle[nx][ny]==float('inf'):
                    if grid[nx][ny]==1:
                        obstacle[nx][ny]=obs+1
                        q.append((obs+1,nx,ny))
                    else:
                        obstacle[nx][ny]=obs
                        q.appendleft((obs,nx,ny))
        return obstacle[row-1][col-1]