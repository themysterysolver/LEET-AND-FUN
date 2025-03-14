class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        print(dp)
        if amount<1:
            return 0
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i and dp[i-coin]!=float('inf'):
                    dp[i]=min(dp[i-coin]+1,dp[i])
        return dp[-1] if dp[-1]!=float('inf') else -1