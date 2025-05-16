class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def lcs(a,b):
            dp=[[0]*(len(a)+1) for _ in range(len(b)+1)]
            for i in range(1,len(dp)):
                for j in range(1,len(dp[0])):
                    if b[i-1]==a[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[-1][-1]
        l=lcs(word1,word2)
        return len(word1)-l+len(word2)-l