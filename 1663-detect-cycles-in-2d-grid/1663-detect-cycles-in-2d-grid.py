class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def display(g):
            for row in g:
                print(row)
            print('------------------------')
        row,col=len(grid),len(grid[0])
        visited=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        display(grid)
        def BFS(r,c,tx):
            #print('-------start------------------------',tx)
            q=deque([(r,c,-1,-1)])
            visited.add((r,c))
            while q:
                x,y,px,py=q.popleft()
                #print(x,y,px,py)
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        continue
                    else:
                        if grid[nx][ny]==tx and (nx,ny) in visited and (nx,ny)!=(px,py):
                            #print('Ah hemmm')
                            #print(nx,ny,px,py,(nx,ny) in visited,(nx,ny)!=(px,py))
                            return True
                        if grid[nx][ny]==tx and (px,py)!=(nx,ny) :
                            #print('ins:',(nx,ny,x,y))
                            q.append((nx,ny,x,y))
                            #print('q-a-ins:',q)
                            visited.add((nx,ny))
                        
        
                #print('q',q)
            #print('-------going to return FALSE--------')
            return False
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and BFS(i,j,grid[i][j]):
                    return True
        return False