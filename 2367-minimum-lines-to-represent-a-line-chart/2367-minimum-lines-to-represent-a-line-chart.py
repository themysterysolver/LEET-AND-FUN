class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        count = 1
        if len(stockPrices) == 1:
            return 0
        if len(stockPrices) == 2:
            return 1
        stockPrices.sort()
        count = 1
        for i in range(2,len(stockPrices)):
            x1, y1 = stockPrices[i-2]
            x2, y2 = stockPrices[i-1]
            x3, y3 = stockPrices[i]
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                count += 1
        return count