class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        while n!=1:
            count=1
            ns=""
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    count+=1
                else:
                    ns+=str(count)+s[i-1]
                    count=1
            ns+=str(count)+s[-1]
            n-=1
            s=ns[:]
        return s

                
