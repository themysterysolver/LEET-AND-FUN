class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        count = 0
        pre = 0
        for num in nums:
            pre+=num
            if pre>0:
                count+=1
            else:
                break
        return count