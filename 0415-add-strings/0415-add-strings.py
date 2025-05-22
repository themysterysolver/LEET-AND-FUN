class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j=len(num1)-1,len(num2)-1
        carry=0
        result=[]
        while i>=0 or j>=0 or carry>0:
            digit1=int(num1[i]) if i>=0 else 0
            digit2=int(num2[j]) if j>=0 else 0
            sumx=digit1+digit2+carry
            result.insert(0,str(sumx%10))
            carry=sumx//10
            #print(result,digit1,digit2,carry,sumx)
            i-=1
            j-=1
        return ''.join(result)