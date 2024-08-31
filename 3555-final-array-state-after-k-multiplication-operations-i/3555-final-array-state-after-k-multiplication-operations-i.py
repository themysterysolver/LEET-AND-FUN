class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while(k!=0):
            ind=nums.index(min(nums))
            nums[ind]=nums[ind]*multiplier
            k-=1
        return nums