class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        par_x=self.find(x)
        par_y=self.find(y)
        if par_x==par_y:
            return
        elif self.rank[par_x]<self.rank[par_y]:
            self.parent[par_x]=par_y
        elif self.rank[par_y]<self.rank[par_x]:
            self.parent[par_y]=par_x
        else:
            self.parent[par_y]=par_x
            self.rank[par_x]+=1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        dsu=DSU(row*col)
        directions=[(0,1),(1,0)] #right,down

        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    for dx,dy in directions:
                        nx,ny=i+dx,j+dy
                        if nx>=row or ny>=col or grid[nx][ny]=='0':
                            continue
                        else:
                            dsu.union(i*col+j,nx*col+ny)
        islands=set()
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    islands.add(dsu.find(col*i+j))
        return len(islands)
