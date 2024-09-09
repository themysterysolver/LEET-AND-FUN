class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gasoline=nums[0]
        if len(nums)==1 :
            return True
        for i in range(1,len(nums)-1):
            gasoline-=1
            if gasoline==-1:
                return False
            if gasoline<nums[i]:
                gasoline=nums[i]
        if gasoline>=1:
            return True
        else:
            return False
        
        