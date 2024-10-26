class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost)
        if len(cost)==1:
            return cost[-1]
        elif len(cost)==2:
            return min(cost[-1],cost[-2])
        else:
            dp[0],dp[1]=cost[0],cost[1]
            for i in range(2,len(cost)):
                dp[i]=cost[i]+min(dp[i-1],dp[i-2])
            return min(dp[-1],dp[-2])