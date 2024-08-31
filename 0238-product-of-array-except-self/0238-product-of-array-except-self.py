class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product=1
        flag=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c=0
            else:
                c=1
                break
        if c==0:
            return nums
        n=nums.count(0)
        print n
        if n>=2:
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=0
            return nums
        for i in range(len(nums)):
            if nums[i]==0:
                flag=1
                continue
            product=product*nums[i]
        for i in range(len(nums)):
            if flag==1 and nums[i]!=0:
                nums[i]=0
            elif flag==1 and nums[i]==0:
                nums[i]=product
            elif flag==0:
                nums[i]=product/nums[i]
        print nums,product
        return nums
        