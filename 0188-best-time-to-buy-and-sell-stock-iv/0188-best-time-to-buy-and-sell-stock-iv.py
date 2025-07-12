class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)

        @cache
        def go(i,holding,rem): # rem - remaining transactions
            if rem==0 or i==n:
                return 0
            if holding:
                return max(go(i+1,True,rem),prices[i]+go(i+1,False,rem-1)) #sell
            else:
                return max(go(i+1,False,rem),-prices[i]+go(i+1,True,rem)) #buy
        return go(0,False,k)