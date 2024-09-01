class Solution:
    def isFascinating(self, n: int) -> bool:
        t=2*n
        tr=3*n
        t=str(t)
        tr=str(tr)
        n=str(n)
        n=n+t+tr
        d=dict()
        for i in n:
            if i=="0":
                return False
            if i not in d:
                d[i]=1
            else:
                return False
        if len(d)==9:
            return True
            
        