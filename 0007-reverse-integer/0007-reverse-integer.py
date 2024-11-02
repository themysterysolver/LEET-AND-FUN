class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            x=-x
            sign=-1
        res=0
        while x!=0:
            res=res*10+x%10
            x=x//10
        return res*sign if res*sign<2**31-1 and res*sign>-2**31 else 0
        