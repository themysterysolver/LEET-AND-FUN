class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('--------------')
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        count=0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        def BFS(r,c):
            nonlocal count
            visited[r][c]=True
            boundary=False
            q=deque([(r,c)])
            lands=0
            while q:
                x,y=q.popleft()
                lands+=1
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        boundary=True
                    else:
                        if grid[nx][ny]==1 and not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny]=True
            if boundary:
                pass 
            else:
                count+=lands
            print(count)
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and not visited[i][j]:
                    BFS(i,j)
        return count 