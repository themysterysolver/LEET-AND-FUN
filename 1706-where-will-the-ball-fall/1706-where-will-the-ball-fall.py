class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def display(mat):
            for row in mat:
                print(row)
            print('---------------')
        display(grid)
        ans = [-1]*len(grid[0])
        r,c = len(grid),len(grid[0])
        def dfs(i,x,y):
            #print(i,x,y)
            if x<0 or y>=c:
                return False
            if x>=r:
                ans[i] = y
                return True
            curr = grid[x][y]
            if curr == 1:
                if y+1<c and grid[x][y+1] == 1:
                    return dfs(i,x+1,y+1)
                else:
                    return False
            else:
                if y-1>=0 and grid[x][y-1] == -1:
                    return dfs(i,x+1,y-1)
                else:
                    return False


        for i in range(len(grid[0])):
            if dfs(i,0,i):
               #print('hollah',i) 
               pass 
        return ans