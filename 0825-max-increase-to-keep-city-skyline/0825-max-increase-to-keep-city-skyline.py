class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = defaultdict(int)
        for i,r in enumerate(grid):
            row[i] = max(r)
        
        col = defaultdict(int)
        for j in range(len(grid[0])):
            maxi = float('-inf')
            for i in range(len(grid)):
                maxi = max(maxi,grid[i][j])
            col[j] = maxi
        
        #print(row)
        #print(col)
        sumx = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans = min(row[i],col[j])-grid[i][j]
                if ans>0:
                    sumx+=ans
        return sumx