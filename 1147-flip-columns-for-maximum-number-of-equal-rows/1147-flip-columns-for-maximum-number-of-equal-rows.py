#analyse that after fliiping to optimum we realise the columns which are similar and complementary give the right answer!
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        maxIdenticalRows=0
        for row in matrix:
            flipped=[1-x for x in row]
            count=0
            for compareRow in matrix:
                if compareRow==row or compareRow==flipped:
                    count+=1
            maxIdenticalRows=max(maxIdenticalRows,count)
        return maxIdenticalRows
