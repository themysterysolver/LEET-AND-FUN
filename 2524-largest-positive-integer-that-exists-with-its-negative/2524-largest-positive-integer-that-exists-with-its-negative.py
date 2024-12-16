class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        #print(nums)
        start,end=0,len(nums)-1
        while start<end:
            if abs(nums[start])==nums[end] and nums[start]!=nums[end]:
                return nums[end]
            elif abs(nums[start])<nums[end]:
                end-=1
            else:
                start+=1
        return -1