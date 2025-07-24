class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        sumx = len(grid) - 1
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i == j or i+j == sumx:
                    if grid[i][j]==0:
                        return False
                else:
                    if grid[i][j]!=0:
                        return False
        return True