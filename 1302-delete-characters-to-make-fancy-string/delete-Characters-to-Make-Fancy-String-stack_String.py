class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:
            return s
        stackString=""
        stackString+=s[0]+s[1]
        print(stackString)
        for i in range(len(s)):
            if i>1:
                if stackString[-1]==s[i] and stackString[-2]==s[i]:
                    continue
                stackString+=s[i]
        return stackString


