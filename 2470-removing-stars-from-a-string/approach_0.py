#didn't check for constraint and did this!!
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        print(list(s))
        for i in range(len(s)):
            print(stack,i-1)
            if s[i]=='*':
                if len(stack)>=1:
                    stack.pop()
                    continue
                else:
                    continue
            stack.append(s[i])
        return ''.join(stack)
