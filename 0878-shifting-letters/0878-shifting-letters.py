class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        toDo=[0]*len(s)
        shift=0
        for i in range(len(s)-1,-1,-1):
            shift+=shifts[i]
            toDo[i]=shift
        print(toDo)
        s=list(s)
        for i in range(len(s)):
            s[i]=chr((ord(s[i])-ord('a')+toDo[i])%26+ord('a'))
        return ''.join(s)
