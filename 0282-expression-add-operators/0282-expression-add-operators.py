class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def backtrack(idx,expr,currVal,prevVal): #path=Expr
            if idx == len(num):
                if currVal == target:
                    res.append(expr)
                return

            for i in range(idx,len(num)):
                if idx!=i and num[idx]=='0':
                    break
                part = num[idx:i+1]
                digit = int(part)
                if idx == 0:
                    backtrack(i+1,expr+part,digit,digit)
                else: 
                    backtrack(i+1,expr+"+"+part,currVal+digit,digit)
                    backtrack(i+1,expr+"-"+part,currVal-digit,-digit)
                    backtrack(i+1,expr+"*"+part,currVal-prevVal+prevVal*digit,digit*prevVal)
        backtrack(0,"",0,0)
        return res