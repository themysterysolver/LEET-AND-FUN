#simulation with recursion and dp
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n=len(nums)
        @cache
        def backtrack(idx):
            if idx==n-1:
                return 0
            maxi=float('-inf')
            for j in range(idx+1,n):
                if -target<=nums[j]-nums[idx]<=target:
                    maxi=max(maxi,backtrack(j)+1)
            return maxi
        return backtrack(0) if backtrack(0)!=float('-inf') else -1