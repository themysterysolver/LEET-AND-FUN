#made error not including all the rotted elements in q!!
#hence now efrom every rotten orange it spreads!!!
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def display(mat):
            for row in mat:
                print(row)
            print('-----------------------')
        def findRotten():
            COUNT=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        COUNT+=1
            return COUNT
        def BFS(r,c):
            row,col=len(grid),len(grid[0])
            visited=[[False]*col for _  in range(row)]
            visited[r][c]=True
            directions=[(0,1),(0,-1),(1,0),(-1,0)]
            rotten=findRotten()
            print('NO OF not ROTTEN:',rotten)
            #rotten-=1
            q=deque([(r,c)])
            #error here!!
            '''for i in range(row):
                  for j in range(col):
                      if not visited[i][j] and grid[i][j]==2:
                          q.append((i,j))
                          visited[i][j]=True'''
            count=0
            print('QUEUE AT',count,'->',list(q))
            while q:
                l=len(q)
                for i in range(l):
                    x,y=q.popleft()
                    for dx,dy in directions:
                        nx,ny=dx+x,dy+y
                        if nx<0 or ny<0 or nx==row or ny==col:
                            continue
                        elif grid[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            rotten-=1
                count+=1
                print('At this COUNT:',count)
                display(visited)
                print('QUEUE AT',count,'->',list(q))
                print('*****************************************************')
            print('at end rotten:',rotten)
            if rotten==0:
                return count-1
            else:
                return -1
        display(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    print('ROTTEN FOUND AT(Starting):',i,j)
                    print('**********************START**************************')
                    return BFS(i,j)
        if findRotten()>0:
            return -1
        return 0
