class Solution:
    def __init__(self):
        self.count=0
        dp=[[float('inf')] for _ in range(len(nums))]
    def permutation(self,nums,cidx,csum,target):
        if cidx==len(nums):
            if csum==target:
                self.count+=1
        else:
            self.permutation(nums,cidx+1,csum+nums[cidx],target)
            self.permutation(nums,cidx+1,csum-nums[cidx],target)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.permutation(nums,0,0,target)
        return self.count
