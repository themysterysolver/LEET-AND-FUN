class Solution:
    def isThree(self, n: int) -> bool:
        if n==2:
            return False
        count=2
        for i in range(2,n):
            if n%i==0:
                count=count+1
                if count>3:
                    return False
        if count==3:
            return True