class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result=[]
        for i in range(1,len(mountain)-1):
            if mountain[i-1]<mountain[i] and mountain[i+1]<mountain[i]:
                result.append(i)
        return result
