class Solution:
    def findFinalValue(self, nums: List[int], orginal: int) -> int:
        while orginal in nums:
            orginal*=2
        return orginal