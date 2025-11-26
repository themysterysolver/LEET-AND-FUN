class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for key,val in c.items():
            if val == 2:
                ans.append(key)
        n = max(nums)
        k = n*(n+1)//2-sum(set(nums))
        if k == 0:
            ans.append(n+1)
        else:
            ans.append(k)
        return ans