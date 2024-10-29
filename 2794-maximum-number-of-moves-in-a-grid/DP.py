class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('-------------------------')
        row,col=len(grid),len(grid[0])
        tabulation=[[-1]*col for _ in range(row)]
        for i in range(row):
            tabulation[i][0]=0
        directions=[(-1,-1),(0,-1),(1,-1)]
        for j in range(1,col):
            for i in range(row):
                for dx,dy in directions:
                    nx,ny=i+dx,j+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        continue
                    elif grid[nx][ny]<grid[i][j]:
                        if tabulation[nx][ny]!=-1:
                            tabulation[i][j]=max(tabulation[nx][ny]+1,tabulation[i][j])
        display(tabulation)
        display(grid)
        maxi=0
        for i in range(row):
            for j in range(col):
                maxi=max(tabulation[i][j],maxi)
        return maxi
