class Solution:
    def myPow(self, x: float, n: int) -> float:
        base=x
        result=1
        power=n
        if n<0:
            power=-n
        while power>0:
            if power&1:
                result*=base
            base*=base
            power>>=1
        if n<0:
            return 1/result
        return result