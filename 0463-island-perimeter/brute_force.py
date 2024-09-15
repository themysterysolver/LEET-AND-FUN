class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if j==0 or grid[i][j-1]==0:#left
                        perimeter+=1
                    if j==len(grid[i])-1 or grid[i][j+1]==0:#right
                        perimeter+=1
                    if i==0 or grid[i-1][j]==0:#above
                        perimeter+=1
                    if i==len(grid)-1 or grid[i+1][j]==0:#below
                        perimeter+=1       
        return perimeter
                        
