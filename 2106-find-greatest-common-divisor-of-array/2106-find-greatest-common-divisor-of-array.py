class Solution:
    def GCD(self,a,b):
        q,r=divmod(a,b)
        print(q,r)
        if r==0:
            return b
        return self.GCD(b,r)
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        l=nums[0]
        h=nums[-1]
        return self.GCD(h,l)
        