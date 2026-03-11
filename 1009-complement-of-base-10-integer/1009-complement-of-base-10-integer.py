class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        bit = 1
        while n>0:
            if n&1 == 0: #n & 1 says if the last bit is 1 or 0,thus saying odd or even
                ans|=bit #we or since bit is going to be 10,100,1000,10000 so on.
            bit<<=1 #we move 1 to the right for OR
            n>>=1 #we Right shift!
        return ans