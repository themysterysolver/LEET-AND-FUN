class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi=1
        mini=1
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count+=1
            else:
                maxi=max(maxi,count)
                count=1
        maxi=max(maxi,count)
        count=1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                count+=1
            else:
                mini=max(mini,count)
                count=1
        mini=max(mini,count)
        return max(maxi,mini)