class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        c=1
        for i in nums:
            if i<=0:
                continue
            elif i!=c:
                return c
            else:
                c+=1
        return c
        