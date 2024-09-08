class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        a=list(set(nums))
        if len(a)==len(nums):
            return False
        return True
        