class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        nums.append(0)
        maxi = 0
        for num in nums:
            if num == 1:
                count+=1
            else:
                maxi = max(maxi,count)
                count = 0
        return maxi