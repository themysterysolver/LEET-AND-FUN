class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff=[0]*(len(nums)+1)
        for l,r in queries:
            diff[l]-=1
            diff[r+1]+=1
        currDec=0
        print(diff)
        for i in range(len(nums)):
            currDec+=diff[i]
            nums[i]+=currDec
        print(nums)
        return all(x<=0 for x in nums)
            
            