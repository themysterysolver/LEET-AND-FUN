class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for c in s:
            stack.append(c)
            if len(stack)>1 and stack[-1]==']' and stack[-2]=='[':
                stack.pop()
                stack.pop()
        return (stack.count(']')+1)// 2