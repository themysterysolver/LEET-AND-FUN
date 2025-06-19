#very similar to max cons 1-iii and consfusion exam 2024
#since 26 alpha there,maybe less we can check to replace ecah char with limit k
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def maxConsReplacement(s,val):
            maxi,start=0,0
            replacements=0
            for i,c in enumerate(s):
                if c!=val:
                    replacements+=1
                while replacements>k:
                    if s[start]!=val:
                        replacements-=1
                    start+=1
                maxi=max(maxi,i-start+1)
            return maxi
        key=list(set(s))
        print(key)
        maxi=0
        for ke in key:
            maxi=max(maxi,maxConsReplacement(s,ke))
        return maxi