class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        l=[True]*n   
        l[0]=l[1]=False
        for i in range(2,int(n**0.5)+1):
            if l[i]:
                for j in range(i*i,n,i):
                    l[j]=False
            i=i+1
        return sum(l)
