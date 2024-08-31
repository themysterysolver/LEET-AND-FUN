class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        l=[True]*n   
        l[0]=False
        l[1]=False
        count=0
        i=2
        while (i*i)<n:
            if l[i]:
                for j in range(2*i,n,i):
                    l[j]=False
            i=i+1
        for i in l:
            if i:
                count=count+1
       
        return  count