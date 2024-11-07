class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        setBit=[0]*24
        for num in candidates:
            for i in range(24):
                if (num & 1<<i)!=0:
                    setBit[i]+=1
        return max(setBit)
