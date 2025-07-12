class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #holding = 1=> I already have a stock , 0=>I don't have a stock
        @cache
        def go(i,holding):
            if i==len(prices):
                return 0
            if holding:
                return max(
                    go(i+1,True), #skip it
                    prices[i]+go(i+1,False) #sell the stock
                    )
            else:
                return max(go(i+1,False), #skip it
                    -prices[i]+go(i+1,True) #buy the stock
                ) 
        return go(0,False)