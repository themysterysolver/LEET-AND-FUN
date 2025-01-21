class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix=[0]*len(grid[0])
        suffix=[0]*len(grid[0])
        suff,pre=0,0
        for i in range(len(grid[0])):
            suff+=grid[0][i]
            suffix[i]=suff
        for i in range(len(grid[0])-1,-1,-1):
            pre+=grid[1][i]
            prefix[i]=pre
        print('{}\n{}'.format(suffix,prefix))
        max1,max2=0,float('inf')
        for i in range(len(grid[0])):
            pathSum=prefix[i]+suffix[i]
            if pathSum>max1:
                maxi=pathSum
                max2=min(max2,max(pre-prefix[i],suff-suffix[i]))
        return max2