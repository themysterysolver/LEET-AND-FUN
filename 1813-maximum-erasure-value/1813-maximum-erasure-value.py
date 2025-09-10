class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        maxi = 0
        start = 0
        sumx = 0
        for i in range(len(nums)):
            while nums[i] in s:
                sumx-=nums[start]
                s.remove(nums[start])
                start+=1
            s.add(nums[i])
            sumx+=nums[i]
            maxi = max(maxi,sumx)
        return maxi
