class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ds=""
        prev=0
        spaces.append(len(s))
        for i in spaces:
            ds+=s[prev:i]+' '
            prev=i
        print(ds)
        return ds[0:-1]