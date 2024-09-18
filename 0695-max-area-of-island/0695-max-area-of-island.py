class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        max_area=0
        def BFS(r,c):
            q=deque([(r,c)])
            area=0
            visited[r][c]=True
            while q:
                area+=1
                x,y=q.popleft()
                for dx,dy in direction:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx==row or ny==col or grid[nx][ny]==0:
                        continue
                    elif grid[nx][ny]==1 and not visited[nx][ny]:
                        visited[nx][ny]=True
                        q.append((nx,ny))
            return area

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j]:
                    max_area=max(max_area,BFS(i,j))
        return max_area