class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi = float('-inf')
        s = set()
        rsum = 0
        for num in nums:
            if num<0:
                maxi = max(num,maxi)
                continue
            if num in s:
                continue
            else:
                rsum += num
                maxi = max(rsum,maxi)
                if rsum<0:
                    s = set()
                    rsum = 0
                    continue
                s.add(num)
        return maxi