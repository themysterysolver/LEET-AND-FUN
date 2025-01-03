class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum=[0]*len(nums)
        suffixSum=[0]*len(nums)
        prefix=suffix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            prefixSum[i]=prefix
        for i in range(len(nums)-1,-1,-1):
            suffix+=nums[i]
            suffixSum[i]=suffix
        #print(prefixSum,suffixSum)
        count=0
        for i in range(len(nums)-1):
            if prefixSum[i]>=suffixSum[i+1]:
                count+=1
        return count