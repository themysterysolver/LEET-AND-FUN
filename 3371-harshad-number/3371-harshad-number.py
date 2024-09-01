class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a=list(map(int,str(x)))
        if x%sum(a)==0:
            return sum(a)
        else:
            return -1