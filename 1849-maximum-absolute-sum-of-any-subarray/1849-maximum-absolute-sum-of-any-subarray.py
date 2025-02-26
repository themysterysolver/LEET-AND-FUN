class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def kadane(nums):
            maxi=float('-inf')
            sumi=0
            for i in nums:
                sumi+=i
                maxi=max(maxi,sumi)
                if sumi<0:
                    sumi=0
            return maxi
        return max(kadane([i*-1 for i in nums]),kadane(nums))