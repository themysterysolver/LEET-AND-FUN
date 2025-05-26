class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for c in s:
            if c=="(":
                stack.append("(")
            else:
                if stack[-1]=="(":
                    stack.pop()
                    stack.append(1)
                elif str(stack[-1]).isdigit() and stack[-2]=="(":
                    el=stack.pop()
                    stack.pop()
                    stack.append(el*2)
                else:
                    score=0
                    while stack[-1]!="(":
                        score+=stack.pop()
                    stack.pop()
                    stack.append(score*2)
            print(c,stack)
        return sum(stack)
