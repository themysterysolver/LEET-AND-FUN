class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        balance=0
        for i in range(len(s)):
            if s[i]=='(' or locked[i]=='0':
                balance+=1
            else:
                balance-=1
            if balance<0:
                return False
        balance=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or locked[i]=='0':
                balance+=1
            else:
                balance-=1
            if balance<0:
                return False
        return True