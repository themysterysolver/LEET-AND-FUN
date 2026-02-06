class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        maxi = float('-inf')
        l = 0
        for r in range(n):
            while nums[l]*k < nums[r]:
                l+=1
            maxi = max(maxi,r-l+1)
        return n-maxi