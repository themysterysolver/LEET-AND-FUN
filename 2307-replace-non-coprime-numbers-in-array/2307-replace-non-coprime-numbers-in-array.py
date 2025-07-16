# LCM * HCF = x * y
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        @cache
        def HCF(x,y):
            if y == 0:
                return x
            return gcd(y,x%y)
        @cache
        def LCM(x,y):
            return x*y // gcd(x,y)
        
        stack = []
        for num in nums:
            while stack and HCF(stack[-1],num)>1:
                num = LCM(stack.pop(),num)
            stack.append(num)
        return stack
