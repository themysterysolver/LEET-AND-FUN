class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        hash=defaultdict(int)
        count=0
        for i,num in enumerate(nums):
            count+=hash[i-num]
            hash[i-num]+=1
        print(count)
        return (len(nums)*(len(nums)-1)//2)-count