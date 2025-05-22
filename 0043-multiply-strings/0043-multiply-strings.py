class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def addStrings(num1: str, num2: str) -> str:
            i,j=len(num1)-1,len(num2)-1
            carry=0
            result=[]
            while i>=0 or j>=0 or carry>0:
                digit1=int(num1[i]) if i>=0 else 0
                digit2=int(num2[j]) if j>=0 else 0
                sumx=digit1+digit2+carry
                result.insert(0,str(sumx%10))
                carry=sumx//10
                ##print(result,digit1,digit2,carry,sumx)
                i-=1
                j-=1
            return ''.join(result)
        def multiplyIt(big,small):
            result=[]
            small=int(small)
            carry=0
            for i in range(len(big)-1,-1,-1):
                ##print(small[i])
                bigN=int(big[i])
                ans=bigN*small+carry
                result.insert(0,str(ans%10))
                carry=ans//10
            if carry!=0:
                result.insert(0,str(carry))
            #print(result)
            return ''.join(result)
        totalSum=[]
        if num1=="0" or num2=="0":
            return "0"
        large=num1 if len(num1)>len(num2) else num2
        small=num2 if len(num1)>len(num2) else num1
        #print("LARGE",large)
        #print("SMALL",small)
        for i in range(len(small)-1,-1,-1):
            totalSum.append(multiplyIt(large,small[i])+"0"*(len(small)-i-1))
        #print(totalSum)
        runningSum="0"
        for x in totalSum:
            runningSum=addStrings(runningSum,x)
        return runningSum