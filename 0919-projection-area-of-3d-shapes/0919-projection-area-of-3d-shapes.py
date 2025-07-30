class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xz = 0
        for row in grid:
            xz += max(row)
        xy , yz = 0,0
        for i in range(len(grid[0])):
            colMax = 0
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    xy += 1
                colMax = max(colMax,grid[j][i])
            yz += colMax
        return xy + yz + xz