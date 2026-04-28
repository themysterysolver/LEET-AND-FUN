#costraints less I will brute it !!!
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dis = lambda x:(print(*x,sep='\n'),print('-------'))
        n = len(grid)
        dp_m = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dp_m[0][i] = grid[0][i]
        #dis(grid)

        @cache
        def dp(x,y):
            if x == n-1:
                return grid[x][y]
            mini = float('inf')
            for i in range(n):
                if i!=y:
                    mini = min(mini,dp(x+1,i))
            return grid[x][y]+mini
        mini = float('inf')
        for i in range(n):
            mini = min(mini,dp(0,i))
        return mini