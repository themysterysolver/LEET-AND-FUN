class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        maxi=0
        nums.sort()
        s=set(nums)
        print(nums)
        @cache
        def go(n):
            if n not in s:
                return 0
            return go(n*n)+1
        #print(go)
        for num in nums:
            maxi=max(maxi,go(num))
        return maxi if maxi>=2 else -1
