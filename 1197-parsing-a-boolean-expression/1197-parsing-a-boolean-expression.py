class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack=[]
        operators={'|','&','!'}
        bools={'t','f'}
        for s in expression:
            if s in operators or s in bools:
                stack.append(s)
            elif s==')':
                contains_true,contains_false=False,False
                while stack[-1] not in operators:
                    top=stack.pop()
                    if top=='t':
                        contains_true=True
                    elif top=='f':
                        contains_false=True
                operator_eval=stack.pop()
                if operator_eval=='!':
                    if contains_true:
                        stack.append('f')
                    elif contains_false:
                        stack.append('t')
                elif operator_eval=='&':
                    if contains_false:
                        stack.append('f')
                    else:
                        stack.append('t')
                else:
                    if contains_true:
                        stack.append('t')
                    else:
                        stack.append('f')
        return stack[-1]=='t'
                
    

        