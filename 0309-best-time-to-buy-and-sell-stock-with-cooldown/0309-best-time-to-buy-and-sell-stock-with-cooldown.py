class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def go(i,holding):
            if i>=n:
                return 0
            if holding:
                return max(go(i+1,True),prices[i]+go(i+2,False))
            else:
                return max(go(i+1,False),-prices[i]+go(i+1,True))
        return go(0,False)