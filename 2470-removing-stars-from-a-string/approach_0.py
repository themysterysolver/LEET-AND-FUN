#didn't check for constraint and did this!!
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=='*':
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
#I honestly don't what's the big difference!!!
