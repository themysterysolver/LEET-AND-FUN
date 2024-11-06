class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        setBits=bin(nums[0]).count('1')
        maxSeg,minSeg=nums[0],nums[0]
        maxPrev=float('-inf')
        for i in range(1,len(nums)):
            if bin(nums[i]).count('1')==setBits:
                maxSeg=max(maxSeg,nums[i])
                minSeg=min(minSeg,nums[i])
            else:
                if minSeg<maxPrev:
                    return False
                maxPrev=maxSeg
                maxSeg,minSeg=nums[i],nums[i]
                setBits=bin(nums[i]).count('1')
        if minSeg<maxPrev:
            return False
        return True
