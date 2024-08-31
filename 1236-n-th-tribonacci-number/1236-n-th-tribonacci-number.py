class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        elif n==2:
            return 1
        a=[0,1,1]
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2]+a[i-3])
        return a[-1]
        