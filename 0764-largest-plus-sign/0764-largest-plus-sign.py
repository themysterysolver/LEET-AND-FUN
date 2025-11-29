class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1]*n for _ in range(n)]
        for x,y in mines:
            grid[x][y] = 0
        m,n = n,n
        left = [[0]*n for _ in range(m)]
        right = [[0]*n for _ in range(m)]
        top = [[0]*n for _ in range(m)]
        down = [[0]*n for _ in range(m)]

        #from left how much?
        for i in range(m):
            count = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 1:
                    count+=1
                else:
                    count = 0
                left[i][j] = count
        
        #from right,how much?
        for i in range(m):
            count = 0
            for j in range(n):
                if grid[i][j] == 1:
                    count+=1
                else:
                    count = 0
                right[i][j] = count
        
        #from top
        for i in range(n):
            count = 0
            for j in range(m):
                if grid[j][i] == 1:
                    count+=1
                else:
                    count = 0
                top[j][i] = count
        
        #from bottom
        for i in range(n):
            count = 0
            for j in range(m-1,-1,-1):
                if grid[j][i] == 1:
                    count+=1
                else:
                    count = 0
                down[j][i] = count
        maxi = 0
        def display(mat):
            for row in mat:
                print(row)
            print('-------------')
        # display(left)
        # display(right)
        # display(top)
        # display(down)
        for i in range(m):
            for j in range(n):
                maxi = max(min(left[i][j],right[i][j],top[i][j],down[i][j]),maxi)
        return maxi
                