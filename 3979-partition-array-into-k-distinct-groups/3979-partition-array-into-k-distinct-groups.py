class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        c = Counter(nums)
        if len(nums)%k != 0:
            return False
        for val in c.values():
            if val>len(nums)//k:
                return False


        return True