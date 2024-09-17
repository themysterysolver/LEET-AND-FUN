class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col=len(grid),len(grid[0])
        visited=[[False]*col for _ in range(row)]
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def DFS(r,c):
            if r<0 or c<0 or r==row or c==col or grid[r][c]==0:
                    return 1
            if visited[r][c]:
                return 0
            visited[r][c]=True
            perimeter=0
            for dx,dy in direction:
                perimeter+=DFS(r+dx,c+dy)
            return perimeter 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return DFS(i,j)
                        