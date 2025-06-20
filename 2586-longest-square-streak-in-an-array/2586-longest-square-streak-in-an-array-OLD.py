class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set=set(nums)
        visited=set([])
        print(nums)
        maxl=0
        for i in nums:
            num=i
            l=1
            while num*num in nums_set and num*num not in visited:
                visited.add(num*num)
                num=num*num
                l+=1
            maxl=max(maxl,l)
            #print(i,visited,maxl)
            #print('------------------')
        return maxl if maxl>=2 else -1
