class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = 0
        smooth = 0
        prices.append(-1)
        for r in range(1,len(prices)):
            if prices[r-1] == prices[r]+1:
                #print('INSIDE:',l,r)
                continue
            else:
                n = r-l
                #print('breakge at',l,r,n)
                smooth += n*(n+1)//2
                l = r
            #print(l,r)
        return smooth