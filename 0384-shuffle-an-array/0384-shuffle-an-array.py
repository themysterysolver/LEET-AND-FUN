class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.use = nums[:]
    def reset(self) -> List[int]:
        self.use[:] = self.nums
        return self.use

    def shuffle(self) -> List[int]:
        random.shuffle(self.use)
        return self.use


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()