#what i did is technically cheating!!
#what I knwo is sorting a string is in lexicographic order,then I mapped to integer!
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans=[str(i) for i in range(1,n+1)]
        ans.sort()
        print(ans)
        ans=map(int,ans)
        return ans
        
