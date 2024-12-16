class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash=dict()
        nums.sort()
        for i in nums:
            hash[i]=hash.get(i-1,0)+1
        return max(hash.values())
        