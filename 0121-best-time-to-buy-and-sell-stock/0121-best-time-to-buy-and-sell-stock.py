class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        flag=1
        for i in range(1,len(prices)):
            if prices[i-1]>prices[i]:
                flag=0
            else:
                flag=1
                break    
        if flag==0:
            return 0
        maxi=0
        mini=99999999
        for i in range(len(prices)):
            if(prices[i]<mini):
                mini=prices[i]
            if(prices[i]-mini>maxi):
                maxi=prices[i]-mini
        '''for i in range(len(prices)):
            if(max(prices[i:])-prices[i]>maxi):
                maxi=max(prices[i:])-prices[i]'''
        '''for i in range(len(prices)):
            buy=prices[i]
            for j in range(i,len(prices)):
                sell=prices[j]
                if(sell-buy>maxi):
                    maxi=sell-buy'''
        return maxi



        