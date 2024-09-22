class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[str(i) for i in range(1,n+1)]
        ans.sort()
        print(ans)
        ans=map(int,ans)
        return ans
        