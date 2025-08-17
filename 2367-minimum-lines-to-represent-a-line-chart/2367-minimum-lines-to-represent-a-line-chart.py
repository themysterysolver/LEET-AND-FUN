class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        count = 1
        if len(stockPrices) == 1:
            return 0
        if len(stockPrices) == 2:
            return 1
        stockPrices.sort()
        count = 1
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        def slope(a,b):
            x1,y1 = a
            x2,y2 = b
            c = y2-y1
            d = x2-x1
            g = gcd(c,d)
            return (c//g,d//g)
        m = slope(stockPrices[0],stockPrices[1])
        for i in range(2,len(stockPrices)):
            if m == slope(stockPrices[i],stockPrices[i-1]):
                continue
            else:
                m = slope(stockPrices[i],stockPrices[i-1])
                count += 1
        return count