class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxi,mini = max(nums),min(nums)
        s,b = nums.index(mini),nums.index(maxi)
        #l,r = 0,len(nums)-1
        return min(max(s,b)+1,
        len(nums)-min(s,b),
        len(nums)-max(s,b)+min(s,b)+1)