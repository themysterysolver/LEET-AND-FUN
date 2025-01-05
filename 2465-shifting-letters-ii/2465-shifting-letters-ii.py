class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s=list(s)
        toDo=[0]*(len(s)+1)
        for start,end,action in shifts:
            if action==0:
                toDo[start]-=1
                toDo[end+1]+=1
            else:
                toDo[start]+=1
                toDo[end+1]-=1
        shift=0
        for i in range(len(toDo)):
            shift+=toDo[i]
            toDo[i]=shift
        #print(toDo)
        for i in range(len(s)):
            s[i]=chr((ord(s[i])-ord('a')+toDo[i])%26+ord('a'))
        #print(s)
        return ''.join(s)