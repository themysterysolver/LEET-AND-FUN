class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic_increasing=nums[:]
        monotonic_decreasing=nums[:]
        monotonic_increasing.sort()
        monotonic_decreasing.sort(reverse=True)
        print(monotonic_increasing, monotonic_decreasing)
        if nums==monotonic_increasing or monotonic_decreasing==nums:
            return True
        else:
            return False 