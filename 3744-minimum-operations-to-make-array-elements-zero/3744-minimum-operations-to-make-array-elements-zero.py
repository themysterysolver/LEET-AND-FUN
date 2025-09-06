class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def helper(n):
            p = 1
            k = 0
            while p <= n:
                k += 1
                p = p << 2
            print(k)
            k-=1
            return (n+1) * (k+1) - (pow(4, k+1) - 1)//3

        cnt = 0
        for l,r in queries:
            cnt += math.ceil((helper(r) - helper(l-1))/2)
        
        return cnt