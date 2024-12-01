class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=0
        deleted=0
        start=0
        for i in range(len(nums)):
            if nums[i]==0:
                deleted+=1
            while deleted>1:
                if nums[start]==0:
                    deleted-=1
                start+=1
            maxi=max(maxi,i-start)
        return maxi
        