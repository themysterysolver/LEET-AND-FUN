class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            print i,sum(nums[:i]),sum(nums[i+1:])
            if(sum(nums[:i])==sum(nums[i+1:])):
                return i
        return -1
        