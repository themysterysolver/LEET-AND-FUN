class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        prefix = [[0]*(n) for _ in range(m)]
        def display(matrix):
            for row in matrix:
                print(row)
            print('-------------------')
        #display(prefix)
        col = 0
        for i in range(m):
            col+=grid[i][0]
            prefix[i][0] = col
        row = 0
        for j in range(n):
            row+=grid[0][j]
            prefix[0][j] = row
        # display(prefix)
        for i in range(1,m):
            for j in range(1,n):
                prefix[i][j] = grid[i][j]+prefix[i][j-1]+prefix[i-1][j]-prefix[i-1][j-1]
        #display(prefix)
        count = 0
        for i in range(m):
            for j in range(n):
                if prefix[i][j]<=k:
                    #print(i,j,prefix[i][j],k,prefix[i][j]<=k)
                    count+=1
        return count