class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=0
        print('s r')
        for right in range(1,len(nums)):
            if nums[right]!=nums[right-1]:
                nums[start+1]=nums[right]
                start+=1
        return start+1