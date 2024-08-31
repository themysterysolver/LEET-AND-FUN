class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=dict()
        a=[]
        for i in nums:
            if i not in d:
                d[i]=1
            elif d[i]<2 :
                d[i]=d[i]+1
                if d[i]==2:
                    a.append(i)
        return a
            
        