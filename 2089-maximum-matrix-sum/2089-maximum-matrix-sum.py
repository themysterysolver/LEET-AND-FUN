class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalsum=0
        negativecount=0
        minAbs=float('inf')
        for row in matrix:
                for i in row:
                    totalsum+=abs(i)
                    if i<0:
                        negativecount+=1 
                    minAbs=min(minAbs,abs(i))
        print(totalsum,minAbs)
        if negativecount%2!=0:
            totalsum-=2*minAbs 
        print(totalsum)
        return totalsum    
       