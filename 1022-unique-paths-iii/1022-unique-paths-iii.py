class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count = [0]
        row,col = len(grid),len(grid[0])
        blocks = set()
        target = row*col
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                elif grid[i][j] == -1:
                    blocks.add((i,j))
        print(blocks)
        target -= len(blocks)+1
        print(target)
        def dfs(r,c,path,t):
            #print(r,c,path,t)
            if grid[r][c] == 2 and t == 0:
                count[0]+=1
                #print("SUCESS",count[0])   
            elif t == 0 or grid[r][c] == 2:
                #print("FAILED")
                return 
            else:
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx,ny = r+dx,c+dy
                    if nx<0 or ny<0 or nx>=row or ny>=col or (nx,ny) in path or (nx,ny) in blocks:
                        continue
                    path.add((nx,ny))
                    dfs(nx,ny,path,t-1)
                    path.remove((nx,ny))
        p,q = start
        dfs(p,q,{start},target)
        return count[0]
                
