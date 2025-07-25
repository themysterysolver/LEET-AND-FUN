class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #using prefix to work the kadane as recurrence thing!
        prefixKadane = [float('-inf')]*len(nums)
        prefixKadane[0] = nums[0]
        for i in range(1,len(nums)):
            prefixKadane[i] = max(nums[i],prefixKadane[i-1]+nums[i])
        return max(prefixKadane)
                
