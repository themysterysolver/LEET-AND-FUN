class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result=[]
        def helper(subset,nums):
            if not nums:
                result.append(subset)
                return
            helper(subset+[nums[0]],nums[1:])
            helper(subset,nums[1:])
        helper([],nums)
        #print(result)
        max_or_value = 0
        count = 0
        for subset in result:
            subset_or = 0
            for num in subset:
                subset_or |= num
            if subset_or > max_or_value:
                max_or_value = subset_or
                count = 1
            elif subset_or == max_or_value:
                count += 1
        return count