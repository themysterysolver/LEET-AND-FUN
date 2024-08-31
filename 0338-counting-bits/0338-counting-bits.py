class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[0]
        for i in range(1,n+1):
            a.append(a[i>>1]+i%2)
        return a