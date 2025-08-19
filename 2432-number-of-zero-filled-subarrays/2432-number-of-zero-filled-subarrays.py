#I got na idea,let's see if it works! since no of subarray for given `n` is n*(n+1)//2 we can simple apply this!
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        start = -1
        count = 0
        nums.append(-1)
        for i in range(len(nums)):
            if nums[i] == 0 and start==-1:
                start = i
            if nums[i]!=0 and start!=-1:
                n = i-start
                start = -1
                count += n*(n+1)//2
        return count
                