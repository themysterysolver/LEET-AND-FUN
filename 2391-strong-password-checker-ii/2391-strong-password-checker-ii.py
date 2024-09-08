class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        p=password[:]
        a=[False]*5
        
        if len(p)>=8:
            a[0]=True
        else:
            return False
        for i in range(len(password)):
            if p[i].isdigit():
                a[3]=True
            if p[i].isupper():
                a[2]=True
            if p[i].islower():
                a[1]=True
            if p[i] in "!@#$%^&*()-+":
                a[4]=True
            if i<len(p)-1 and p[i]==p[i+1]:
                return False
        print(a)
        if False in a:
            return False
        else:
            return True
                
            