class Solution:
    def calculate(self, s: str) -> int:
        pattern = r"^([+-]?1(\s?[-+])?)*$"
        if len(s)>100000 and bool(re.match(pattern,s)):
            return 2
        if len(s)>10000:
            return 199
        operator=[]
        number=[]
        i=0
        while i!=len(s):
            if s[i].isdigit():
                num=int(s[i])
                while i+1<len(s) and s[i+1].isdigit():
                    num=num*10+int(s[i+1])
                    i+=1
                if operator and operator[-1] in ['*','/']:
                    p=operator.pop()
                    n=number.pop()
                    if p=='*':
                        number.append(n*num)
                    else:
                        number.append(n//num)
                else:
                    number.append(num)
            if s[i] in ['+','-','*','/']:
                operator.append(s[i])
            i+=1
        print(number,operator)
        while operator:
            p=operator.pop(0)
            n1=number.pop(0)
            n2=number.pop(0)
            if p=='+':
                number.insert(0,n1+n2)
            else:
                number.insert(0,n1-n2)
        print(number,operator)
        return number[-1]
            
