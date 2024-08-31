class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=nums
        print(nums)
        b=list(set(b))
        print(b)
        b.sort()
        print(b)
        nums[:]=b
        #print(nums)
        return len(nums)
        