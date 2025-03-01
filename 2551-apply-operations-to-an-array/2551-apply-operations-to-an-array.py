class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result=[]
        count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for i in nums:
            if i!=0:
                result.append(i)
        return result+[0]*(len(nums)-len(result))
