class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        maxi=0
        while i<=j:
            maxi=max(maxi,nums[i]+nums[j])
            i+=1
            j-=1
        return maxi
            