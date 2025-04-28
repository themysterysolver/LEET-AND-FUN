class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        def BFS(r,c):
            q=deque([(r,c)])
            visited[r][c]=True
            while q:
                x,y=q.popleft()
                for dx,dy in direction:
                    nx,ny=dx+x,dy+y
                    if nx<0 or ny<0 or nx==row or ny==col or grid[nx][ny]=='0':
                        continue
                    elif grid[nx][ny]=='1' and not visited[nx][ny]:
                        visited[nx][ny]=True
                        q.append((nx,ny))
        
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and not visited[i][j]:
                    count+=1
                    BFS(i,j)
        return count
