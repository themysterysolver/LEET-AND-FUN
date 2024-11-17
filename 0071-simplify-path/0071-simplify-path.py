class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for i in path:
            if i=='/' and len(stack)>=3 and stack[-1]=='.' and stack[-2]=='.' and stack[-3]=='/':
                print('hello!')
                count=0
                while True and stack:
                    if stack[-1]=='/':
                        count+=1
                    if count==2:
                        break
                    stack.pop()
            if i=='/' and len(stack)>=2 and stack[-1]=='.' and stack[-2]=='/':
                stack.pop()
            if i=='/' and stack and stack[-1]=='/':
                continue
            stack.append(i)
            #print(stack)
        if len(stack)>=3 and stack[-1]=='.' and stack[-2]=='.' and stack[-3]=='/':
            count=0
            while True and stack:
                    if stack[-1]=='/':
                        count+=1
                    if count==2:
                        break
                    stack.pop()
        if len(stack)>=2 and stack[-1]=='.' and stack[-2]=='/':
                stack.pop()
        if stack and stack[-1]=='/':
            stack.pop()
        if not stack:
            stack.append('/')
        return ''.join(stack)