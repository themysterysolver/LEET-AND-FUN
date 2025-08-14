class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        maxi = ""
        for i in range(1,len(nums)-1):
            if nums[i-1] == nums[i] == nums[i+1]:
                maxi = max(maxi,nums[i]*3)
        return maxi