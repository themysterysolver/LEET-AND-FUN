class Solution:
    def clumsy(self, n: int) -> int:
        nums = [str(i) for i in range(n,0,-1)]
        idx = 0
        s = nums[0]
        arr = ["*","/","+","-"]
        for i in range(1,len(nums)):
            s+=arr[idx]+nums[i]
            idx = (idx+1)%4
        print(s)
        p ={"+":1,"-":1,"*":2,"/":2}
        def solve(s):
            stack = [ ]
            op = [ ]
            d = 0
            for c in s:
                if c in "*+/-":
                    stack.append(d)
                    d = 0
                    while op and p[op[-1]]>=p[c]:
                        ope = op.pop()
                        e1 = stack.pop()
                        e2 = stack.pop()
                        if ope == "*":
                            stack.append(e1*e2)
                        elif ope == "/":
                            stack.append(e2//e1)
                        elif ope == "+":
                            stack.append(e1+e2)
                        else:
                            stack.append(e2-e1)
                    op.append(c)
                else:
                    d*=10
                    d+=int(c)
                # print(c)
                # print(stack)
                # print(op)
                # print('---------------')
            stack.append(d)
            if len(stack)>1:
                while op:
                    ope = op.pop()
                    e1 = stack.pop()
                    e2 = stack.pop()
                    if ope == "*":
                        stack.append(e1*e2)
                    elif ope == "/":
                        stack.append(e2//e1)
                    elif ope == "+":
                        stack.append(e1+e2)
                    else:
                        stack.append(e2-e1)
            return stack[0]
        return solve(s)