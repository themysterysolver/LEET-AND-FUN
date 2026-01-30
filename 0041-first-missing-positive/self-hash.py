#here we use -ve as an examples to assign positivity!
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        n = len(nums)
        if n == 1 and len(nums) == 1:
            return 2
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]>n:
                nums[i] = 1
        for i in range(len(nums)):
            if nums[i]>0 and nums[nums[i]-1]>0:
                nums[nums[i]-1]*=-1
            if nums[i]<0 and nums[-1*nums[i]-1]>0:
                nums[-1*nums[i]-1]*=-1
        #print(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return n+1
        
