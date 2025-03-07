class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right<2:
            return [-1,-1]
        if right==2:
            return [-1,-1]
        n=right+1
        prime=[True]*(n)
        prime[0]=prime[1]=False
        i=2
        result=[]
        while(i*i<n):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=False
            i+=1
        result=[]
        for i in range(left,n):
            if prime[i]:
                result.append(i)
        print(result)
        ans=[-1,-1]
        if len(result)==1:
            return ans
        if len(result)==2:
            return result
        diff=float('inf')
        for i in range(1,len(result)):
            if diff>result[i]-result[i-1]:
                ans=[result[i-1],result[i]]
                diff=result[i]-result[i-1]
        return ans        