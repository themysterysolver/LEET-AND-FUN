class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=sorted(list(set(letters)))
        print(l)
        for x in l:
            #print(x,ord(target)-ord(x),ord(target)-ord(x)>0)
            if ord(x)-ord(target)>0:
                return x
        return letters[0]