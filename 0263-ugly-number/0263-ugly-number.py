class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if n<0:
            return False
        while n%5==0:
            n=n/5
        while n%3==0:
            n=n/3
        while n%2==0:
            n=n/2
        
        
        print n
        if n==1:
            return True
        else:
            return False
        
        
       
            
        
        
            

        
        