class Solution(object):
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        o=[]
        def helper(nums,subset):
            if not nums:
                o.append(subset[:])
                return
            helper(nums[1:],subset+[nums[0]])
            helper(nums[1:],subset)
        helper(nums,[])
        return o
