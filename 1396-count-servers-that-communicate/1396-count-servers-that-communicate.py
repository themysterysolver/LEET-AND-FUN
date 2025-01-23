class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('------------------')
        display(grid)
        row,col=len(grid),len(grid[0])
        hashR=[0]*row
        hashC=[0]*col
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    hashR[i]+=1
                    hashC[j]+=1
        print(hashR,'\n',hashC)
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1 and (hashR[i]>1 or hashC[j]>1):
                    count+=1
        return count 
        