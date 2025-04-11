class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for x in range(low,high+1):
            if len(str(x))%2==0:
                n=(int(math.log10(x))+1)//2 if x!=0 else 1
                s=str(x)
                if sum(map(int,list(s[:n])))==sum(map(int,list(s[n:]))):
                    count+=1
        return count
                