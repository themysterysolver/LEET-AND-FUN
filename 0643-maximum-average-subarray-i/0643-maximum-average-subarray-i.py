class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # maxi = 0
        sumx = 0
        for i in range(k):
            sumx+=nums[i]
        maxi = sumx/k

        for i in range(k,len(nums)):
            sumx-=nums[i-k]
            sumx+=nums[i]
            maxi = max(maxi,sumx/k)
        return maxi