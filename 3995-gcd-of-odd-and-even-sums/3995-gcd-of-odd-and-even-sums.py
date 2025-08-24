# sum(an) = n//2 * 2a+(n-1)*d
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        odd = n/2*(2*1+(n-1)*2)
        even = n/2*(2*2+(n-1)*2)
        print(odd,even)
        return int(gcd(odd,even))