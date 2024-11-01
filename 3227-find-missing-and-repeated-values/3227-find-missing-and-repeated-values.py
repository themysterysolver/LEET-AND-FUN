class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash=dict()
        for row in grid:
            for i in row:
                if i not in hash:
                    hash[i]=1
                else:
                    hash[i]+=1
        ans=[]
        for key,val in hash.items():
            if val==2:
                ans.append(key)
                break
        val=list(hash.keys())
        print(val)
        n=len(grid)
        print((n*(n+1))//2,sum(val))
        ans.append(n*n*(n*n+1)//2-sum(val))
        return ans
