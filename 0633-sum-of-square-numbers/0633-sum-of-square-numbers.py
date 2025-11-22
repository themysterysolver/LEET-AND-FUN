class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b = 0,int(math.sqrt(c))+1
        while a<=b:
            nc = a*a + b*b
            if nc == c:
                return True
            elif nc>c:
                b-=1
            else:
                a+=1
        return False