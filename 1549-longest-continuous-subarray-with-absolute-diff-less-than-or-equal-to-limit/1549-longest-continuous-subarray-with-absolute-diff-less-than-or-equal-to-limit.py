class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s=SortedList()
        i=0
        maxi=0
        for j in range(len(nums)):
            s.add(nums[j])
            while s and s[-1]-s[0]>limit:
                s.remove(nums[i])
                i+=1
            maxi=max(maxi,j-i+1)
        return maxi
            