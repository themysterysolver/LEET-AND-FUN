class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s =set()
        ans = 0
        for num in nums:
            if num in s:
                ans^=num
            else:
                s.add(num)
        return ans