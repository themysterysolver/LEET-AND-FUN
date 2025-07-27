class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        arr = []
        for i in range(len(nums)):
            if arr:
                if arr[-1]!=nums[i]:
                    arr.append(nums[i])
            else:
                arr.append(nums[i])
        print(arr)
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
                #print(i)
                count += 1
        return count