class Solution:
    def calculate(self, s: str) -> int:
        
        
        ns = ""
        for c in s:
            if c == " ":
                continue
            else:
                ns+=c

        op = []
        num = []
        curr = 0
        
        ns+="+0"

        for c in ns:
            
            if c == "(":
                op.append(c)
            elif c == ")":
                num.append(curr)
                curr = 0
                #print('YOU ENTERED THE ZONE')
                while op and op[-1]!="(":
                    #print(op)
                    #print(num)
                    o = op.pop()
                    num1,num2 = num.pop(),num.pop()
                    if o == "+":
                        num.append((num1+num2))
                    else:
                        num.append((num2-num1))
                curr = num.pop()
                op.pop()
            elif c == "+" or c == "-":
                
                if op and op[-1] == "-":
                    num.append(curr*(-1))
                    op.pop()
                    op.append('+')
                else:
                    num.append(curr)
                
                op.append(c)
                curr = 0
            else:
                curr*=10
                curr+=int(c)
            #print(c)
            #print(num)
            #print(op)
            #print('------------------')
        num.append(curr)
        #print(op)
        #print(num)
        #numer = 0
        while op:
            o = op.pop()
            num1,num2 = num.pop(),num.pop()
            if o == "+":
                num.append((num1+num2))
            else:
                num.append((num2-num1))
        print(num)
        return num[0]





