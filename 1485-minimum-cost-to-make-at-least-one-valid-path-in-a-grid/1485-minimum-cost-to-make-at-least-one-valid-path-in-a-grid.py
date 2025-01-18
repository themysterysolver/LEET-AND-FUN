class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('---------------------')
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        row,col=len(grid),len(grid[0])
        q=[(0,0,0)]
        cm=[[float('inf')]*col for _ in range(row)]
        cm[0][0]=0
        #display(grid)
        #display(cm)
        while q:
            cost,x,y=heapq.heappop(q)
            if cost>cm[x][y]:
                continue
            for c,(dx,dy) in enumerate(directions):
                nx,ny=x+dx,y+dy
                if nx<0 or ny<0 or nx>=row or ny>=col:
                    continue
                newCost=cost
                if grid[x][y]-1!=c:
                    newCost+=1
                if cm[nx][ny]>newCost:
                    cm[nx][ny]=newCost
                    heapq.heappush(q,(newCost,nx,ny))
        #display(cm)
        return cm[-1][-1]


