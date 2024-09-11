class Solution:
    def jump(self, nums: List[int]) -> int:
        totalJump=0
        bound=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i==bound:
                bound=farthest
                totalJump+=1
        return totalJump

        