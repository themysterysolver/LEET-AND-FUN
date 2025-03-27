class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l=len(nums)
        left=[0]*l
        right=[0]*l
        left[0],right[-1]=nums[0],nums[-1]
        for i in range(1,len(nums)):
            left[i]=max(nums[i],left[i-1])
        for i in range(len(nums)-2,-1,-1):
            right[i]=min(nums[i],right[i+1])
        #print(left,right)
        for i in range(1,l):
            if left[i-1]<=right[i]:
                return i
