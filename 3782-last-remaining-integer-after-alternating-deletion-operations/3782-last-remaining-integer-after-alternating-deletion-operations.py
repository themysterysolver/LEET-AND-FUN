class Solution:
    def lastInteger(self, n: int) -> int:
        start = 1
        diff = -1
        l = n
        while l>1:
            diff*=-2
            l = (l+1)//2   
            start = start+(l-1)*diff     
        return start