class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def startBFSknight(grid):
            q=deque([(0,0)])
            row,col=len(grid),len(grid[0])
            visited=[[False]*col for _ in range(row)]
            visited[0][0]=True
            directions=[(1,2),(2,1),(1,-2),(2,-1),(-1,-2),(-2,-1),(-1,2),(-2,1)]
            count=row*col
            while q:            
                l=len(q)
                for i in range(l):
                    x,y=q.popleft()
                    for dx,dy in directions:
                        nx,ny=x+dx,y+dy
                        if nx<0 or ny<0 or nx>=row or ny>=col or visited[nx][ny]:
                            continue
                        elif grid[nx][ny]==grid[x][y]+1:
                            q.append((nx,ny))
                            visited[nx][ny]=True
                            break
                count-=1
            return True if count==0 else False
        return startBFSknight(grid)