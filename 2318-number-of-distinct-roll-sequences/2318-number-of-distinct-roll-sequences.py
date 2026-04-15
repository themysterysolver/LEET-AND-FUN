class Solution:
    def distinctSequences(self, n: int) -> int:
        MOD = 10**9+7
        def gcd(a,b):
            return a if b == 0 else gcd(b,a%b)
        @cache
        def dp(prev,idx,prev_prev):
            if idx == n:
                return 1
            count = 0
            for i in range(1,7):
                if gcd(prev,i)==1 and i!=prev and i!=prev_prev:
                    count=(count+dp(i,idx+1,prev))%MOD
            return count
        count = 0
        for i in range(1,7):
            count=(count+dp(i,1,-1))%MOD
        return count
            
