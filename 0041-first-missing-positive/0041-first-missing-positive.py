class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        current=1
        for i in nums:
            if i<=0:
                continue
            elif i!=current:
                return current
            else:
                current+=1
        return current
        