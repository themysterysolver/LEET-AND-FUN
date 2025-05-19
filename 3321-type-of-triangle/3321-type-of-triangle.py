class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c=nums
        if not(a+b>c and a+c>b and b+c>a):
            return "none"
        if len(set(nums))==1:
            return "equilateral"
        elif len(set(nums))==2:
            return "isosceles"
        else:
            return "scalene"