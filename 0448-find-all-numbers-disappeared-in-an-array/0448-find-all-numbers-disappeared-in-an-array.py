class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen=[False]*len(nums)
        for i in nums:
            seen[i-1]=True
        return [i+1 for i in range(len(nums)) if not seen[i]]