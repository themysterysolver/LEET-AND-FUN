class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxi = 0
        l = len(nums)
        visited = set()
        for i in range(len(nums)):
            j = i
            count = 0
            
            while j not in visited:
                visited.add(j)
                j = nums[j]
                count+=1
            maxi = max(maxi,count)
        return maxi