class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ds=""
        prev=0
        for i in spaces:
            ds+=s[prev:i]+' '
            prev=i
        ds+=s[prev:]
        return ds
