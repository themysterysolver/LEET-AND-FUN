class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        print('Before',nums)
        nums.sort()
        print('After',nums)
        low,high=0,len(nums)-1
        count=0
        i=0
        print('i\t l \t  h \tc\t  s ')
        while low<high:
            print(i,'\t',low,'\t',high,'\t',count,'\t',nums[low]+nums[high])
            i+=1
            if nums[low]+nums[high]==k:
                count+=1
                low+=1
                high-=1
            elif nums[low]+nums[high]<k:
                low=low+1
            elif nums[low]+nums[high]>k:
                high=high-1
        print('LAST C:',count)
        return count
        