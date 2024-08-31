class Solution(object):
    def romanToInt(self, s):
        num=0
        i=0
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i<len(s):
            print i
            if s[i]=='I' and i<len(s)-1:
                if s[i+1]=='V':
                    i=i+2
                    num=num+4
                    continue
                elif s[i+1]=='X':
                    i=i+2
                    num=num+9
                    continue
            elif s[i]=='X'and i<len(s)-1:
                if s[i+1]=='L':
                    i=i+2
                    num=num+40
                    continue
                elif s[i+1]=='C':
                    i=i+2
                    num=num+90
                    continue
            elif s[i]=='C'and i<len(s)-1:
                if s[i+1]=='D':
                    i=i+2
                    num=num+400
                    continue
                elif s[i+1]=='M':
                    i=i+2
                    num=num+900
                    continue
            num+=d[s[i]]
            i+=1
            #num+=d[s[i]]
            #i+=1
        return num