class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(nums)
        start,end=0,len(nums)-1
        print('s e m')
        while start<=end:
            mid=(start+end)//2
            print(start,end,mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
        return -1