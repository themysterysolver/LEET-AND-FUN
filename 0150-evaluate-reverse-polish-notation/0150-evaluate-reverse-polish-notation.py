class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i in {'*','-','+','/'}:
                if i=='*':
                    stack.append(stack.pop()*stack.pop())
                elif i=='-':
                    num1=stack.pop()
                    num2=stack.pop()
                    stack.append(num2-num1)
                elif i=='+':
                    stack.append(stack.pop()+stack.pop())
                else:
                    num1=stack.pop()
                    num2=stack.pop()
                    stack.append(int(num2/num1))
            else:
                stack.append(int(i))
            #print(stack,i)
        return stack[-1]