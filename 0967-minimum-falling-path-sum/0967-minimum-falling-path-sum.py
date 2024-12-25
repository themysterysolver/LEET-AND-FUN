class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def display(msg,matrix):
            print(msg)
            for row in matrix:
                print(row)
            print('--------------')
        row,col=len(matrix),len(matrix[0])
        directions=[(1,1),(1,-1),(1,0)]
        dp=[[float('inf')]*col for _ in range(row)]
        for i in range(col):
            dp[0][i]=matrix[0][i]
        for i in range(row-1):
            for j in range(col):
                for dx,dy in directions:
                    nx,ny=dx+i,dy+j
                    if nx<0 or ny<0 or nx>=row or ny>=col:
                        continue
                    else:
                        dp[nx][ny]=min(dp[nx][ny],dp[i][j]+matrix[nx][ny])
        display('final',dp)
        return min(dp[-1])