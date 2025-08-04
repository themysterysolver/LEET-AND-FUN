#let's try to make the right zeros! coz we are increasing! only way to reduce the sum if to make digits zero! optimally choosing the right to make zero makes sense if we do it in middle it may notbe the smallest!
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        i = 10
        def find_sum(n):
            sumx = 0
            while n!=0:
                sumx += n%10
                n//=10
            return sumx
        diff = 0
        ans = 0
        while True:
            x = find_sum(n)
            print('SUMX:',x)
            if x<=target:
                return ans
            val = n%i
            diff = i - val
            ans = ans + diff
            print('DIFF VAL',diff,val)
            n = n+diff
            print('new n',n)
            i*=10
            