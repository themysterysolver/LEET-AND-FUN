class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<3:
            return -1
        pre = 0
        maxi = 0
        for num in nums:
            if pre>num:
                maxi = max(maxi,pre+num)
            pre+=num
            #print(num,pre,maxi)
        return maxi if maxi!=0 else -1