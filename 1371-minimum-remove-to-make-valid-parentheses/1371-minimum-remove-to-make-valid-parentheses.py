class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]==')':
                stack.append((s[i],i))
                if len(stack)>1 and stack[-1][0]==')' and stack[-2][0]=='(':
                    stack.pop()
                    stack.pop()
        print(stack)
        list_s=list(s)
        for i in stack[::-1]:
            list_s.pop(i[1])
        s=''.join(list_s)
        return s
