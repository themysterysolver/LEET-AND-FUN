class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxCount=0
        for i in range(24):
            count=0
            for num in candidates:
                if (num & 1<<i)!=0:
                    count+=1
            maxCount=max(count,maxCount)
        return maxCount