class Solution(object):
    def subsets(self, nums):
        result=[]
        def helper(nums,subset):
            if not nums:
                result.append(subset[:])
                return
            helper(nums[1:],subset+[nums[0]])
            helper(nums[1:],subset)
        helper(nums,[])
        return result