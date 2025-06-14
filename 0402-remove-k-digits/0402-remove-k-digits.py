class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return "0"
        stack=[]
        for c in num:
            while stack and k!=0 and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        while k>0:
            stack.pop()
            k-=1
        s=''.join(stack)
        s=s.lstrip('0') 
        return s if s else "0"