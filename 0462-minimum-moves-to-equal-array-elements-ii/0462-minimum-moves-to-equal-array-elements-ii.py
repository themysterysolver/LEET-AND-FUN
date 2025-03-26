class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)
        median=nums[l//2]
        count=0
        for i in nums:
            count+=abs(i-median)
        return count