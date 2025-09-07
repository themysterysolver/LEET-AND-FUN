class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n&1 == 1:
            ans.append(0)
            n-=1
        
        while n>0:
            ans.append(n)
            ans.append(-n)
            n-=2
        return ans