class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sum_total=sum(nums)
        if sum_total%p==0:
            return 0
        target=sum_total%p
        min_len=n=len(nums)
        current_sum=0
        modmap={0:-1}
        for i in range(n):
            current_sum=(current_sum+nums[i])%p
            needed=(current_sum-target+p)%p
            if needed in modmap:
                min_len=min(min_len,i-modmap[needed])
            modmap[current_sum]=i
        return -1 if min_len==n else min_len
