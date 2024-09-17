class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def BFS(r,c):
            perimeter=0
            q=deque([(r,c)])
            visited[r][c]=True
            while q:
                x,y=q.popleft()
                for dx,dy in direction:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx==row or ny==col or grid[nx][ny]==0:
                        perimeter+=1
                    elif grid[nx][ny]==1 and not visited[nx][ny]:
                        visited[nx][ny]=True
                        q.append((nx,ny))
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return BFS(i,j)
                        