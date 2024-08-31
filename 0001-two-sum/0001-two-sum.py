class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
    """
        sumi=0
        for i in range(0,len(nums)):
            sumi=0
            b=[]
            sumi=sumi+nums[i]
            b.append(i)
            for j in range(i+1,len(nums)):
                if(sumi+nums[j]==target):
                    b.append(j)
                    return b
        
        