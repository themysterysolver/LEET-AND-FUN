class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count=0
        bset=set(banned)
        for i in range(1,n+1):
            if i in bset:
                continue
            if maxSum-i<0:
                continue
            maxSum-=i
            count+=1
            if maxSum==0:
                return count
            print(i,count,maxSum)
        return count