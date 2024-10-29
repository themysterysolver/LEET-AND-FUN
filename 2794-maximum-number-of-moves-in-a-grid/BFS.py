class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in grid:
                print(row)
            print('------------------------')
        def modBFS():
            q=deque([])
            row,col=len(grid),len(grid[0])
            directions=[]
            for i in range(row):
                q.append((i,0))
            visited=[[False]*col for _ in range(row)]
            directions=[(-1,1),(0,1),(1,1)]
            print(list(q))
            count=0
            while q:
                l=len(q)
                for i in range(l):
                    x,y=q.popleft()
                    #print('----------++---------\n',"x,y",x,y)
                    for dx,dy in directions:
                        nx,ny=x+dx,y+dy
                        #print('NX,NY',nx,ny)
                        if nx<0 or ny<0 or nx>=row or ny>=col or visited[nx][ny]:
                            continue
                        elif grid[nx][ny]>grid[x][y]:
                            #print('grid[nx][ny]',grid[nx][ny])
                            visited[nx][ny]=True
                            q.append((nx,ny))
                #print('qlist--->',list(q))
                count+=1
            return count-1
        display(grid)
        return modBFS()
