class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left,right=0,len(nums)
        while left<=right:
            mid=(left+right)//2
            if mid!=0 and mid!=len(nums)-1:
                if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                    return mid
                elif nums[mid+1]>nums[mid]:
                    left=mid+1
                elif nums[mid-1]>nums[mid]:
                    right=mid-1
            else:
                if len(nums)==1:
                    return 0
                print(mid)
                if mid==0:
                    if nums[mid+1]<nums[mid]:
                        return 0
                    else:
                        left=mid+1
                elif mid==len(nums)-1:
                    if nums[mid-1]<nums[mid]:
                        return len(nums)-1
                    else:
                        right=mid-1
            