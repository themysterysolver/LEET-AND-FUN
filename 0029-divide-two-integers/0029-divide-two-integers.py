class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign=-1 if(dividend>=0 and divisor<0) or (dividend<0 and divisor>0) else 1
        dividend=abs(dividend)
        divisor=abs(divisor)
        result=len(range(0,dividend-divisor+1,divisor))
        result=-result if sign==-1 else result
        result=min(max(result,-2**31),2**31-1)
        return result