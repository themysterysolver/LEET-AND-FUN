class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [math.comb(rowIndex,j) for j in range(rowIndex+1)]



        