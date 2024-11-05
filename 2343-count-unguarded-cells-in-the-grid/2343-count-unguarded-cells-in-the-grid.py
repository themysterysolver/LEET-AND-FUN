class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('-----------------')
        def countUnguard(mat):
            count=0
            for row in mat:
                for element in row:
                    if element==" ":
                        count+=1
            return count 
        grid=[[" "]*n for _ in range(m)]
        #display(grid)
        for r,c in walls:
            grid[r][c]="W"
        #display(grid)
        for r,c in guards:
            grid[r][c]="G"
        #display(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="G":
                    #RIGHT
                    for k in range(j+1,n):
                        if grid[i][k]=="W" or grid[i][k]=="G":
                            break
                        else:
                            grid[i][k]="B"
                    #LEFT
                    for k in range(j-1,-1,-1):
                        if grid[i][k]=="W" or grid[i][k]=="G":
                            break
                        else:
                            grid[i][k]="B"
                    #DOWN
                    for k in range(i+1,m):
                        if (grid[k][j]=="W" or grid[k][j]=="G"):
                            break
                        else:
                            grid[k][j]="B"
                    #UP
                    for k in range(i-1,-1,-1):
                        if grid[k][j]=="W" or grid[k][j]=="G":
                            break
                        else:
                            grid[k][j]="B"
        #display(grid)
        count=countUnguard(grid)
        return count