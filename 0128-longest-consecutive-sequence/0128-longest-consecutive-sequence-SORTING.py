class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=list(set(nums))
        nums.sort()
        print(nums)
        l=1
        maxi=0
        for i in range(len(nums)):
            if i>0 and nums[i]-nums[i-1]==1:
                l+=1
            else:
                maxi=max(l,maxi)
                l=1
        return max(l,maxi)
        
