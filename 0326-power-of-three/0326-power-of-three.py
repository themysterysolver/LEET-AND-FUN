class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n==3:
            return True
        if n<=2:
            return False
        if n%3==0:
            return self.isPowerOfThree(n/3)
        
        
        