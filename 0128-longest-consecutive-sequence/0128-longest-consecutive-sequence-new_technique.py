#O(N) ,brilliant solution by naga!
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        s = set(nums)
        for num in s:
            if num-1 not in s:
                count = 0
                while num in s:
                    count+=1
                    num+=1
                maxi=max(maxi,count)
        return maxi
        
