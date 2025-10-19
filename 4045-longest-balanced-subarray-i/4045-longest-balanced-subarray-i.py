class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        maxi = 0
        for i in range(len(nums)):
            odd,even = set(),set()
            for j in range(i,len(nums)):
                if nums[j]%2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(odd) == len(even):
                    maxi = max(maxi,j-i+1)
        return maxi