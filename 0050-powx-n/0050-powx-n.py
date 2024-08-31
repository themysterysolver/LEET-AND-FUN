class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            print n
            return 1
        if n==1:
            print x
            return x
        if n<0:
            return 1/self.myPow(x,-n)
        half=self.myPow(x,n/2)
        print half,half*half
        if n%2==0:
            return half*half
        else:
            return half*x*half
        
            
        
        