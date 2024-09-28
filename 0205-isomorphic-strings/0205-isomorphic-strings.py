class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
            elif s[i] in d:
                if d[s[i]]==t[i]:
                    continue
                else:
                    return False
        duplicate=d.values()
        if len(duplicate)==len(set(duplicate)):
            return True
        else:
            return False