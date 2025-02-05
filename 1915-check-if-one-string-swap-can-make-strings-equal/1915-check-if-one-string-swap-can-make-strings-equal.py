class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        c1,c2=Counter(s1),Counter(s2)
        if c1!=c2 or len(s1)!=len(s2):
            return False
        print(c1,c2)
        diff=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
        return diff<=2
