class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        flag=False
        for i in range(len(nums)):
            if flag:
                if nums[i]<=nums[(i+1)%len(nums)]:
                    continue
                return False
            else:
                if nums[i]<=nums[(i+1)%len(nums)]:
                    continue
                else:
                    flag=True
                    if nums[i]>=nums[(i+1)%len(nums)]:
                        continue
                    return False
        return True
