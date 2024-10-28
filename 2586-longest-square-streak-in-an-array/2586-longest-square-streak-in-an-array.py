class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        maxlen=0
        map=dict()
        for n in nums:
            sqroot=int(math.sqrt(n))
            if sqroot*sqroot==n and sqroot in map:
                map[n]=map[sqroot]+1
                maxlen=max(maxlen,map[n])
            else:
                map[n]=1
        return maxlen if maxlen>=2 else -1
        