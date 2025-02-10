class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isnumeric():
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
            
