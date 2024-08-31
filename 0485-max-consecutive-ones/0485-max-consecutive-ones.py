class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        maxi=0
        for i in nums:
            if i==1:
                c=c+1
                if(c>maxi):
                    maxi=c
            else:
                c=0
        return maxi
        