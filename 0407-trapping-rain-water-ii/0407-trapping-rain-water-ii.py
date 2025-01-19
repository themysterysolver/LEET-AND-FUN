class Solution:
    def display(self,mat):
        for row in mat:
            print(row)
        print('-------------------')
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.display(heightMap)
        water=0
        grid=heightMap
        row,col=len(grid),len(grid[0])
        if row<3 or col<3:
            return 0
        #Initial setup
        visited=[[False]*col for _ in range(row)]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        heap=[]
        #Let's push borders into heap
        for i in range(row):
            for j in range(col):
                if i==0 or i==row-1 or j==0 or j==col-1:
                    heapq.heappush(heap,(grid[i][j],i,j))
                    visited[i][j]=True
        '''print(heap)'''
        #handlers
        level=0
        water=0
        #heap-BFS-simulation-Flooding
        while heap:
            lvl,x,y=heapq.heappop(heap)
            level=max(lvl,level)
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col or visited[nx][ny]:
                    continue
                else:
                    if grid[nx][ny]<level:
                        water+=level-grid[nx][ny]
                    heapq.heappush(heap,(grid[nx][ny],nx,ny))
                    visited[nx][ny]=True
        return water

        