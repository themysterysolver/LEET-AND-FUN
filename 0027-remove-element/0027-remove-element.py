class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        print(nums,val,nums.count(val))
        b=nums.count(val)
        #print(nums.count(val))
        while(nums.count(val)):
            nums.remove(val)
            print(nums,val)
        return len(nums)
        