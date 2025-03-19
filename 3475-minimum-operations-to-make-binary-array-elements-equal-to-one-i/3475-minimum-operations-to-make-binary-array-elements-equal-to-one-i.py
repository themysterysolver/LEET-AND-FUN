class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in  range(len(nums)-2):
            if nums[i]==0:
                count+=1
                for j in range(3):
                    if nums[i+j]==0:
                        nums[i+j]=1
                    else:
                        nums[i+j]=0
        #print(nums)
        if 0 in nums:
            return -1
        else:
            return count