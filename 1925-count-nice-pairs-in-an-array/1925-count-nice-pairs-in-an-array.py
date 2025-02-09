class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        hash=defaultdict(int)
        count=0
        mod=10**9+7
        for i,num in enumerate(nums):
            count=(count+hash[num-rev(num)])%mod
            hash[num-rev(num)]+=1
        return count