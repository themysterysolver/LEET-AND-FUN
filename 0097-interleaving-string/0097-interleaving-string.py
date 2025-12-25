class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,last = len(s1),len(s2),len(s3)
        if s1 == s2 == s3 == "":
            return True
        if m+n!=last or s3 == "":
            return False
        
        @cache
        def dp(l,r,idx):
            if l==m and r==n and idx == last:
                return True
            if l>=m:
                if s2 and s2[r]!=s3[idx]:
                    return False
                return dp(l,r+1,idx+1)
            if r>=n:
                if s1 and s1[l]!=s3[idx]:
                    return False
                return dp(l+1,r,idx+1)
            ans = False
            if s1 and s1[l] == s3[idx]:
                ans = dp(l+1,r,idx+1)
                if ans:
                    return ans
            if s2 and s2[r] == s3[idx]:
                ans = dp(l,r+1,idx+1)
                if ans:
                    return ans
            return False
        return dp(0,0,0)