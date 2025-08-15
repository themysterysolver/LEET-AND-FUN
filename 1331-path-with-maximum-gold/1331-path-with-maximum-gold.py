class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        visited = set()

        def dfs(r,c):
            if r<0 or c<0 or r>=row or c>=col or grid[r][c] == 0 or (r,c) in visited:
                return 0
            cost = float('-inf')
            visited.add((r,c))
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx,ny = r+dx,c+dy
                cost = max(cost,grid[r][c]+dfs(nx,ny))
            visited.remove((r,c))
            return cost
        
        maxi = float('-inf')
        for i in range(row):
            for j in range(col):
                maxi = max(maxi,dfs(i,j))
                #print(i,j,dfs(i,j))
        return maxi