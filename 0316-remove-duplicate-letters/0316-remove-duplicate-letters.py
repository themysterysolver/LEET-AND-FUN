class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        last_idx={c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1]>c and last_idx[stack[-1]]>i:
                stack.pop()
            stack.append(c)
        return ''.join(stack)