# PEAK LOGIC,TRUST ME BRUH!
# SEE WE CAN USE DSU TO minimse BFS
# Here if we think from forward pov eveything is hard,u need to do BFS very single time,so what can we do?
# Reverse it!
# Hell yeah,go from backward populate land instead of water. If u got bottom and top in same parent,yup you got it bruhh!
# Let's code some Union-find!
# thinknig it back indexing is a much cooler idea! than hashing!
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)] #dict()
        self.rank = [0]*n #dict()
    
    def find(self,x):
        # if x not in self.parent:
        #     self.parent[x] = x
        #     self.rank[x] = 0
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        rx,ry = self.rank[px],self.rank[py]
        if rx<ry:
            self.parent[py] = px
        elif rx>ry:
            self.parent[px] = py
        else:
            self.rank[px]+=1
            self.parent[px] = py

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row*col
        top = n
        bottom = n+1
        dsu = DSU(n+2)
        idx = lambda r,c: r*col+c
        grid = [[1]*col for _ in range(row)]
        for x,y in cells:
            grid[x-1][y-1] = 1
        #populating all from top!
        # q = deque([])
        # for i in range(col):
        #     if grid[0][i] == 0:
        #         q.append((0,i))
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        # while q:
        #     x,y = q.popleft()
        #     dsu.union(top,idx(x,y))
        #     for dx,dy in dir:
        #         nx,ny = x+dx,y+dy
        #         if nx<0 or ny<0 or nx>=row or ny>=col or grid[nx][ny] == 1:
        #             continue
        #         q.append((nx,ny))
        # #from bottom
        l_days = len(cells)
        # q = deque([])
        # for i in range(col):
        #     if grid[-1][i] == 0:
        #         q.append((row-1,i))
        # dir = [(0,1),(1,0),(0,-1),(-1,0)]
        # while q:
        #     x,y = q.popleft()
        #     dsu.union(bottom,idx(x,y))
        #     if dsu.find(top) == dsu.find(bottom):
        #         return l_days
        #     for dx,dy in dir:
        #         nx,ny = x+dx,y+dy
        #         if nx<0 or ny<0 or nx>=row or ny>=col or grid[nx][ny] == 1:
        #             continue
        #         q.append((nx,ny))
        print(dsu.parent)
        '''That's why u read the q proprly!! Ther whole grid is going to be island only at EOD of cells sso let's add Land!'''
        
        for i,(x,y) in enumerate(cells[::-1]):
            x,y = x-1,y-1
            curr = idx(x,y)
            grid[x][y] = 0
            if x == 0:
                dsu.union(top,idx(x,y))
            if x == row-1:
                dsu.union(bottom,idx(x,y))
            for dx,dy in dir:
                nx,ny = x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col or grid[nx][ny] == 1:
                    continue
                dsu.union(curr,idx(nx,ny))
            if dsu.find(top) == dsu.find(bottom):
                return l_days-i-1
        

            