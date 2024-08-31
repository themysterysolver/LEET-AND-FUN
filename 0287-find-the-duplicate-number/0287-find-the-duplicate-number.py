class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        nums.sort()
        print nums
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]

        