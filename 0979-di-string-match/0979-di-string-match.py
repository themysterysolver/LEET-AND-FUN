class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l,h=0,len(s)
        result=[]
        for c in s:
            if c=='I':
                result.append(l)
                l+=1
            else:
                result.append(h)
                h-=1
        return result+[l]
