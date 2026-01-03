#bro the diagram confused me.
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        type_a,type_b = 6,6 #type-a => 2colour ,type-b => 3colour
        for row in range(2,n+1):
            x = (type_a*3+type_b*2)%mod
            y = (type_a*2+type_b*2)%mod
            type_a = x
            type_b = y
        return (type_a+type_b)%mod
