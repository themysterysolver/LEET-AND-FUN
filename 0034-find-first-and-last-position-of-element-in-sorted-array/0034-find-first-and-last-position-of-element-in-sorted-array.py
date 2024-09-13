class Solution:
    def leftMost(self,nums,target):
        index=-1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                index=mid
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return index
    def rightMost(self,nums,target):
        index=-1
        start,end=0,len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                index=mid
                start=mid+1
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[0,0]
        result[0]=self.leftMost(nums,target)
        result[1]=self.rightMost(nums,target)
        return result