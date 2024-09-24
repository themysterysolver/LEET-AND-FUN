class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=t[:]
        for i in s:
            if i in s and i in n:
                print(i,n)
                n=n[n.index(i)+1:]
                continue
            else:
                return False
        return True
