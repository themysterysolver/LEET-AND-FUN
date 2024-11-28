class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        def display(mat):
            for row in mat:
                print(row)
            print('--------------')
        row,col=len(grid),len(grid[0])
        healthy=[[float('inf')]*col for _ in range(row)]
        healthy[0][0]=health-grid[0][0]
        health-=grid[0][0]
        q=deque([(health,0,0)])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        display(grid)
        display(healthy)
        while q:
            h,x,y=q.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col:
                    continue
                if healthy[nx][ny]==float('inf'):
                    if grid[nx][ny]==0:
                        healthy[nx][ny]=h
                        q.appendleft((h,nx,ny))
                    else:
                        healthy[nx][ny]=h-1
                        q.append((h-1,nx,ny))
        display(healthy)
        return True if healthy[row-1][col-1]>0 else False