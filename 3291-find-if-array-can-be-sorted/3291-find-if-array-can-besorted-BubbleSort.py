class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        hash=dict()
        for n in nums:
            hash[n]=bin(n).count('1')
        print(hash)
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j+1]<nums[j]:
                    if hash[nums[j+1]]==hash[nums[j]]:
                        nums[j+1],nums[j]=nums[j],nums[j+1]
                    else:
                        return False
        return True
