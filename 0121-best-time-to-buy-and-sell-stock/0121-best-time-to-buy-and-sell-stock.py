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
        return maxi



        