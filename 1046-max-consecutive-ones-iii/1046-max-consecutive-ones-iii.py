class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zero_flipped=0
        maxi=0
        start=0
        print nums
        for i in range(len(nums)):
            if(nums[i]==0):
                zero_flipped=zero_flipped+1
            while(zero_flipped>k):
                if(nums[start]==0):
                    zero_flipped=zero_flipped-1
                start=start+1
            maxi=max({maxi,i-start+1})
        return maxi
        