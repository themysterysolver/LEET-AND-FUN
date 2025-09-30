class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def dis(i,stack,d):
            print(i,formula[i])
            print(stack)
            print(d)
        def cal(idx):
            num = 0
            while idx<end and formula[idx].isdigit():
                num*=10
                num+=int(formula[idx])
                idx+=1
            return num
        stack = []
        i = 0
        end = len(formula)
        d = defaultdict(int)
        while i<end:
            
            if formula[i].isalpha():
                el = formula[i]
                if i == end-1:
                    d[formula[i]]+=1
                    stack.append(d)
                    break
                while 'a'<=formula[i+1]<='z':
                    el += formula[i+1]
                    i+=1
                if formula[i+1].isdigit():
                    d[el] += cal(i+1)
                elif formula[i+1] == '(' or 'A'<=formula[i+1]<='Z' or formula[i+1] == ')':
                    d[el]+=1 
            elif formula[i] == '(':
                stack.append(d)
                stack.append({formula[i]:1})
                d =defaultdict(int)
            elif formula[i] == ')':
                stack.append(d)
                #print('Inner check:')
                #print('STACK:',stack)
                #print('COUNTER',d)
                d = defaultdict(int)
                if i == end-1:
                    break
                if formula[i+1].isdigit():
                    bigd = defaultdict(int)
                    nd = cal(i+1)
                    while '(' not in stack[-1]:
                        cd = stack.pop()
                        for key,val in cd.items():
                            bigd[key]+=val*nd
                    stack.pop()
                    stack.append(bigd)  
                    #print('DOUBLE CHECK:')
                    #print('S check',stack)
                    #print('d check',d)
                else:
                    bigd = defaultdict(int)
                    while '(' not in stack[-1]:
                        cd = stack.pop()
                        for key,val in cd.items():
                            bigd[key]+=val
                    stack.pop() 
                    stack.append(bigd)
            if i == end-1 and not stack:
                stack.append(d) 
            dis(i,stack,d)         
            i+=1
        #print('----------------')
        print(stack)
        bigd = defaultdict(int)
        while stack:
            el = stack.pop()
            for key,val in el.items():
                bigd[key]+=val
        res = ""
        for key,val in sorted(list(bigd.items())):
            if key == '(':
                continue
            res+=key
            if val!=1:
                res+=str(val)
        return res 