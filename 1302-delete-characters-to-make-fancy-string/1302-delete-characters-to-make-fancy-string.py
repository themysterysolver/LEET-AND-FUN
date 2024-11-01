class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        s=list(s)
        prev1,prev2=s[0],s[1]
        for i in range(len(s)):
            if i>1:
                if s[i]==prev1 and s[i]==prev2:
                    s[i]=''
                else:
                    prev1=s[i]
                    prev2=s[i-1]
        return ''.join(s)