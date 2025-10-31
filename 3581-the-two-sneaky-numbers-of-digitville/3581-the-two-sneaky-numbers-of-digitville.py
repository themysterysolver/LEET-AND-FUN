class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for key,val in c.items():
            if val == 2:
                ans.append(key)
        return ans