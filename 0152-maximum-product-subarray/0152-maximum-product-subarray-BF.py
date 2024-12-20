class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=float('-inf')
        for i in range(len(nums)):
            product=nums[i]
            maxi=max(product,maxi)
            for j in range(i+1,len(nums)):
                product*=nums[j]
                maxi=max(product,maxi)
                if product==0:
                    break
        return maxi
