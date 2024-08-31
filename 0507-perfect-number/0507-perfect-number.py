class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        a=[1]
        if num<0:
            return False
        for i in range(2,(int)(math.sqrt(num))+1): #if 1 we will  be including the n itself!
            if num%i==0:
                a.append(i)
                if i!=num//i:
                    a.append(num//i)
        print (a)
        return sum(a)==num
        