class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for val in c.values():
            if val%2==1:
                return False
        return True