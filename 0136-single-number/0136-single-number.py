class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=dict()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in d:
            if d[i]==1:
                return i
        