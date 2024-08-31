class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        nums.sort()
        maxi=0
        for i in range(len(nums)-1):
            if maxi<nums[i+1]-nums[i]:
                maxi=nums[i+1]-nums[i]
        return maxi
        