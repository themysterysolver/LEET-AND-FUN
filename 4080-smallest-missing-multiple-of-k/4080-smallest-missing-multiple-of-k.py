class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        num = k
        while num in s:
            num+=k
        return num