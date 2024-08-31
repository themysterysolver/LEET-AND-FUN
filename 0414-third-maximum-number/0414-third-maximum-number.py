class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        nums.sort()
        l=list(set(nums))
        l.sort()
        print l
        if len(l)==3 or len(l)==1:
            return l[0]
        if len(l)==2:
            print l[1]
            return l[1]
        return l[len(l)-3]
        
        