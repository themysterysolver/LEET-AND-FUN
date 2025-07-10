# derive the recuurrence relation
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,2,5]
        mod=10**9+7
        if n<3:
            return dp[n-1]
        for i in range(3,n+1):
            dp.append((2*dp[i-1] + dp[i-3])%mod)
        return dp[-2] 