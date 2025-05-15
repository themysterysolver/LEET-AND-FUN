class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def display(mat):
            for row in mat:
                print(row)
            print('--------------')
        m,n=len(word1),len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(len(dp[0])):
            dp[0][i]=i
        for j in range(len(dp)):
            dp[j][0]=j
        display(dp)
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        display(dp)
        return dp[n][m]