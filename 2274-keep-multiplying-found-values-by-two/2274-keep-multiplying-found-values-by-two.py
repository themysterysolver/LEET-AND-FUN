class Solution:
    def findFinalValue(self, nums: List[int], orginal: int) -> int:
        nums.sort()
        idx = -1 if orginal not in nums else nums.index(orginal)
        while idx!=-1:
            orginal*=2
            idx = -1 if orginal not in nums else nums.index(orginal)

        return orginal