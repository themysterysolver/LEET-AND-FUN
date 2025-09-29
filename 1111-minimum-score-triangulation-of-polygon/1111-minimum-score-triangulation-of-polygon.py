class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(i,j):
            if i+2>j:
                return 0
            if i+2 == j:
                return values[i]*values[i+1]*values[i+2]
            return min(values[i]*values[k]*values[j]+dp(i,k)+dp(k,j) for k in range(i+1,j))
        return dp(0,len(values)-1)