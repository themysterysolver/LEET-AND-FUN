class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        l = len(nums)
        for i in range(len(nums)):
            visited = set()
            visited.add(i)
            if (i+nums[i])%l == i:
                continue
            curr = (i+nums[i])%l
            dir = "P" if nums[i]>0 else "N"
            if (dir=="P" and nums[curr]<0 ) or (dir == "N" and nums[curr]>0):
                continue
            visited.add(curr)
            while curr!=(curr+nums[curr])%l:
                if (dir=="P" and nums[curr]<0 ) or (dir == "N" and nums[curr]>0):
                    break
                curr = (curr+nums[curr])%l
                if curr in visited:
                    return True
                visited.add(curr)
        return False