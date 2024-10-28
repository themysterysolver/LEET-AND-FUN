class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums=set(nums)
        maxlen=0
        for n in nums:
            num=n
            l=1
            while num*num in nums:
                l+=1
                num*=num
            maxlen=max(maxlen,l)
        return maxlen if maxlen>=2 else -1
        