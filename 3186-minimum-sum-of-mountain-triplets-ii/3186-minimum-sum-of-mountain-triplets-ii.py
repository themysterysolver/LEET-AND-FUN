class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minSum=float('inf')
        n=len(nums)
        left=[float('inf')]*n
        right=[float('inf')]*n
        for i in range(1,n):
            left[i]=min(nums[i-1],left[i-1])
        for j in range(n-2,-1,-1):
            right[j]=min(nums[j+1],right[j+1])
        for i in range(1,len(nums)-1):
            if left[i]<nums[i] and right[i]<nums[i]:
                minSum=min(minSum,nums[i]+left[i]+right[i])
        return minSum if minSum!=float('inf') else -1