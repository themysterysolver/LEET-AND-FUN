class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder=preorder.split(',')
        stack=[]
        for c in preorder:
            if c!="#":
                stack.append(c)
            else:
                while stack and stack[-1]=="#":
                    stack.pop()
                    if not stack:
                        return False
                    stack.pop()
                stack.append(c)
            #print(stack)
        if len(stack)==1 and stack[0]=='#':
            return True
        else:
            return False