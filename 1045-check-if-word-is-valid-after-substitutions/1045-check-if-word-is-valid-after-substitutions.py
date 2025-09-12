#stack a,b,c
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack)<2:
                stack.append(c)
            else:
                if c == 'c' and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(c)
            #print(c,stack)
        #print(stack)
        return len(stack) == 0