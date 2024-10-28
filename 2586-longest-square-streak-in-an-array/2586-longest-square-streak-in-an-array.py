class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set=set(nums)
        visited=set([])
        print(nums)
        maxl=0
        for i in nums:
            c=i
            l=1
            while c*c in nums_set and c*c not in visited:
                visited.add(c*c)
                c=c*c
                l+=1
            maxl=max(maxl,l)
            #print(i,visited,maxl)
            #print('------------------')
        return maxl if maxl>=2 else -1
        