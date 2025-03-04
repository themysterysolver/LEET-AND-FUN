class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=1
        print('s r')
        for right in range(1,len(nums)):
            if nums[right]!=nums[right-1]:
                nums[start]=nums[right]
                start+=1
        return start