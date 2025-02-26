class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        sumi=0
        for i in nums:
            sumi+=i
            maxi=max(maxi,sumi)
            if sumi<0:
                sumi=0
        return maxi
                