class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nums = bin(n)[2:]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return False
        return True