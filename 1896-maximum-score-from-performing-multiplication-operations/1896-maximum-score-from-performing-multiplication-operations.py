class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n,m=len(nums),len(multipliers)
        
        @cache
        def go(l,r,idx):
            if idx==m:
                return 0
            return max(go(l+1,r,idx+1)+nums[l]*multipliers[idx],go(l,r-1,idx+1)+nums[r]*multipliers[idx])
        return go(0,n-1,0)