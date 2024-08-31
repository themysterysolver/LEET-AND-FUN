class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)+1
        print l
        d=dict()
        for i in range(l):
            d[i]=False
        print d
        for i in nums:
            if i in d:
                d[i]=True
        print d
        for i in d:
            if d[i]==False:
                return i
       
        