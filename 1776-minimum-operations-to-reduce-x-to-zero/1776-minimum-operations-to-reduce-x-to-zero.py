# let's chnage the perspective of the question!
# instead of finding the min count,we can find the max subbary size where sum is sum(nums)-x
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        left,right,sumx = 0,0,0
        maxi = -1
        while right<len(nums):
            sumx+=nums[right]
            while sumx>target:
                sumx-=nums[left]
                left+=1
            if sumx == target:
                maxi = max(maxi,right-left+1)
            right+=1
        return -1 if maxi == -1 else len(nums)-maxi