class Solution:
    def partitionString(self, s: str) -> int:
        sett=set()
        count=0
        for e in s:
            if e in sett:
                sett=set()
                count+=1
            sett.add(e)
        return count+1