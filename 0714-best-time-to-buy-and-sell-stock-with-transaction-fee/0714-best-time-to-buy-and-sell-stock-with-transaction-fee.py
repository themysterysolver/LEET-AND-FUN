class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #similiar to BS-II
        n = len(prices)
        @cache
        def go(i,holding):
            if i==n:
                return 0
            if holding:
                return max(go(i+1,True),prices[i]+go(i+1,False))
            else:
                return max(go(i+1,False),-prices[i]-fee+go(i+1,True))
        return go(0,False)
