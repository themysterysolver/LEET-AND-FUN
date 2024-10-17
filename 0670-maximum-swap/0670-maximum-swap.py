class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=list(map(int,str(num)))
        #print(nums)
        max_pos=[0]*len(nums)
        max_pos[-1]=len(nums)-1
        max_pt=len(nums)-1
        for i in  range(len(nums)-2,-1,-1):
            if nums[i]>nums[max_pt]:
                max_pos[i]=i
                max_pt=i
            else:
                max_pos[i]=max_pt
        #print(max_pos)

        for i in range(len(nums)):
            if nums[i]>=nums[max_pos[i]]:
                continue
            else:
                nums[i],nums[max_pos[i]]=nums[max_pos[i]],nums[i]
                break

        return int(''.join(map(str,nums)))