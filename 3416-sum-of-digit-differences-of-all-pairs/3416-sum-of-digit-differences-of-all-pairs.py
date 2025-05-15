class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        l=len(str(nums[0]))
        print(l,nums[0],str(nums[0]),len(str(nums[0])))
        count=0
        n=len(nums)
        for i in range(l):
            c=Counter([str(num)[i] for num in nums])
            for v in c.values():
                count+=v*(n-v)
        return count//2
        
