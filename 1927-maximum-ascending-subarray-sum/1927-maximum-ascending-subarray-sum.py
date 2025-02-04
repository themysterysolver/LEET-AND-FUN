class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi=float('-inf')
        sumi=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                sumi+=nums[i]
            else:
                maxi=max(maxi,sumi)
                sumi=nums[i]
            print(i,sumi,maxi)
        maxi=max(maxi,sumi)
        return maxi
