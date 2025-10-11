class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count = 0
        sumx = 0
        for num in nums:
            sumx+=num
            if sumx == 0:
                count+=1
        return count