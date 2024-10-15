class Solution:                                  #Black-1 , White-0......Black to right and white to left!
    def minimumSteps(self, s: str) -> int:
        if '1' not in s:
            return 0
        if '0' not in s:
            return 0
        count=0
        s=list(s)
        while s.index('1')<len(s)-1-s[::-1].index('0'):
            for i in range(len(s)-1,-1,-1):
                if s[i]=='0':
                    pass
                else:
                    if i!=len(s)-1 and s[i+1]=='0':
                        s[i]='0'
                        s[i+1]='1'
                        break
            #print(s)
            count+=1
        return count
        
