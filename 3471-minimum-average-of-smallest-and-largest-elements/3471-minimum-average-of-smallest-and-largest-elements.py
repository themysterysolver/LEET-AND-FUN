class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        av=[]
        #nums=list(set(nums))
        while(len(nums)):
            ma=max(nums)
            mi=min(nums)
            nums.remove(ma)
            nums.remove(mi)
            av.append((float(ma+mi)/2))
            #print nums,(ma+mi)/2
        return min(av)
        