class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        o=[]
        nums.sort()
        def helper(nums,subset):
            if not nums:
                o.append(subset[:])
                return 
            helper(nums[1:],subset+[nums[0]])
            helper(nums[1:],subset)
        helper(nums,[])
        print o
        o=list(map(list, set(map(tuple,o))))
        return o