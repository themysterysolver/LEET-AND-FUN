class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def display(mat):
            for row in grid:
                print(row)
            print('-------------------')
        display(grid)
        def BFS(r,c):
            start=grid[r][c]
            row,col=len(grid),len(grid[0])
            visited=[[False]*col for _ in range(row)]
            q=deque([(r,c)])
            directions=[(1,0),(0,1),(0,-1),(-1,0)]
            visited[r][c]=True
            toBorder=[]
            if start==color:
                return
            #print('initial',list(q))
            while q:
                x,y=q.popleft()
                isBorder=False
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        isBorder=True
                    elif grid[nx][ny]!=start:
                        isBorder=True
                    elif not visited[nx][ny] and grid[nx][ny]==start:
                        visited[nx][ny]=True
                        q.append((nx,ny))
                if isBorder:
                    toBorder.append((x,y))
                print(list(q))
                display(grid)
            for x,y in toBorder:
                grid[x][y]=color
        BFS(row,col)
        return grid