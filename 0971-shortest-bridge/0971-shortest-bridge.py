class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        def display(mat):
            for row in mat:
                print(row)
            print('--------------')
        def BFS(r,c):
            visited=set()
            border=set()
            q=deque([(r,c)])
            visited.add((r,c))
            border.add((r,c))
            directions=[(0,1),(1,0),(0,-1),(-1,0)]
            while q:
                #print(q)
                x,y=q.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    #print((nx,ny))
                    if nx<0 or ny<0 or nx>=row or  ny>=col or (nx,ny) in visited:
                        continue
                    else:
                        if grid[nx][ny]==1:
                            q.append((nx,ny))
                            visited.add((nx,ny))
                            if nx==0 or ny==0 or nx==row-1 or ny==col-1:
                                border.add((nx,ny))
                            elif not (grid[nx-1][ny]==1 and grid[nx+1][ny]==1) and not (grid[nx][ny+1]==1 and grid[nx][ny-1]==1):
                                border.add((nx,ny))
                #print('------------------------',x,y)
            print('BORDER:',border,len(border))
            #li=list(border)
            #print("Border-sort:",li)
            q=deque(border)
            count=0
            while q:
                l=len(q)
                for _ in range(l):
                    x,y=q.popleft()
                    for dx,dy in directions:
                        nx,ny=x+dx,y+dy
                        if nx<0 or ny<0 or nx>=row or ny>=col or (nx,ny) in visited:
                            continue
                        else:
                            if grid[nx][ny]==1:
                                return count
                            q.append((nx,ny))
                            visited.add((nx,ny))
                count+=1
        display(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return BFS(i,j)       