class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('--------------')
        row,col=len(matrix),len(matrix[0])
        dp=[[0]*(col) for _ in range(row)]
        flag=False
        for r in range(row):
            for c in range(col):
                if matrix[r][c]=='1':
                    flag=True
                    matrix[r][c]=1
                else:
                    matrix[r][c]=0
        if not flag:
            return 0
        maxi=1
        #display(matrix)
        #population
        for r in range(row):
            dp[r][0]=matrix[r][0]
        #display(dp) 
        for c in range(col):
            dp[0][c]=matrix[0][c]
        #display(dp)
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxi=max(dp[i][j],maxi)
        #display(dp)
        return maxi**2
