class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        score=0
        for bit in range(32):
            count=sum((num>>bit & 1) for num in nums)
            score+=(len(nums)-count)*count
        return score
            
