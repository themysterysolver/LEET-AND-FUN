class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def calSum(k):
            nums = arr[:]
            for i in range(len(arr)):
                if nums[i]>k:
                    nums[i] = k
            return sum(nums)
        
        mini = float('inf')
        left,right = 1,max(arr)
        while left<=right:
            mid = (left+right)//2
            if calSum(mid)>target:
                right = mid-1
            else:
                left = mid+1
        if abs(calSum(left) - target) < abs(calSum(left - 1) - target):
            return left
        else:
            return left - 1