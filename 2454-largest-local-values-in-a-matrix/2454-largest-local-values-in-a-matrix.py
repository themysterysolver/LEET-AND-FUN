class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def find_loc(grid,x,y):
            maxi=float('-inf')
            for i in range(3):
                for j in range(3):
                    maxi=max(maxi,grid[x+i][y+j])
            return maxi
        n=len(grid)
        result=[[0]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                result[i][j]=find_loc(grid,i,j)
        return result