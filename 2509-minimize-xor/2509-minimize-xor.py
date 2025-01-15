class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1,n2=list(map(int,list(bin(num1)[2:]))),list(map(int,list(bin(num2)[2:])))
        print(n1,n2)
        if len(n1)>len(n2):
            n=len(n1)-len(n2)
            n2=[0]*n+n2
        else:
            n=len(n2)-len(n1)
            n1=[0]*n+n1
        print(n1,n2)
        count2=n2.count(1)
        result=[0]*len(n1)
        for i in range(len(result)):
            if n1[i]==1 and count2!=0:
                result[i]=1
                count2-=1
        print('checkpt1',result,count2)
        if count2>0:
            for i in range(len(result)-1,-1,-1):
                if result[i]==0:
                    result[i]=1
                    count2-=1
                    if count2==0:
                        break
        
        j=0
        x=0
        for i in range(len(result)-1,-1,-1):
            if result[i]==1:                    
                x+=2**j
            j+=1
        return x
        
            

        
        