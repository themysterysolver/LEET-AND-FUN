class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        sumMin=float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]<nums[j] and nums[k]<nums[j]:
                        sumMin=min(sumMin,nums[i]+nums[j]+nums[k])
        return sumMin if sumMin!=float('inf') else -1