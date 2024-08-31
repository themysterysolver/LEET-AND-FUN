class Solution:
    def addDigits(self, num: int) -> int:
        temp=num
        sum=0
        while True:
            print (sum,temp)
            if temp==0:
                if sum>=10:
                    temp=sum
                    sum=0
                else:
                    return sum
            sum=sum+temp%10
            temp=temp//10