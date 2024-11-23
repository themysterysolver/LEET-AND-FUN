class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq=dict()
        for row in matrix:
            pattern=''.join('T' if i==row[0] else 'F' for i in row)
            freq[pattern]=freq.get(pattern,0)+1
        return max(freq.values())
