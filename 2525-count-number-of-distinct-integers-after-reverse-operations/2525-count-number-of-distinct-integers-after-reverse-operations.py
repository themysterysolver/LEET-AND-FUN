class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = nums[:]
        def rev(num):
            ans = 0
            while num!=0:
                ans*=10
                ans+=num%10
                num//=10
            return ans
        for i in s:
            nums.append(rev(i))
        return len(set(nums))