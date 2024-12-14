class Solution:
    def reorderSpaces(self, text: str) -> str:
        strArray=text.split(" ")
        print(strArray)
        spaces=text.count(' ')
        words=list(filter(None,strArray))
        print(words,spaces,len(words)-1)
        if len(words)==1:
            return words[0]+" "*spaces
        lspaces=spaces//(len(words)-1)
        s=""
        print(lspaces)
        for i in range(len(words)):
            if i!=len(words)-1:
                s+=words[i]+(" ")*lspaces
            elif i==len(words)-1:
                s+=words[i]
        print(s)
        rem=spaces%(len(words)-1)
        print(rem)
        return s if rem==0 else s+" "*rem
