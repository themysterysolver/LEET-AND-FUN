class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        nums = list(c.items())
        nums = [val for key,val in nums]
        nums.sort(reverse=True)
        count = 0
        #print(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                count+=1
                nums[i]-=1
            elif nums[i-1]<nums[i]:
                neww = max(nums[i-1]-1,0)
                count+=(nums[i]-neww)
                nums[i] = neww
            #print(i,nums)
        #print('---------------')
        #print(nums)
        return count
