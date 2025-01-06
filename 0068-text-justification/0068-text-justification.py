class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result=[]
        currentLine=[]
        noOfLettersInCurrentLine=0
        for word in words:
            if noOfLettersInCurrentLine+len(currentLine)+len(word)>maxWidth:
                vacantSpaces=maxWidth-noOfLettersInCurrentLine
                for i in range(vacantSpaces):
                    currentLine[i%(len(currentLine)-1 or 1)]+=' '
                result.append(''.join(currentLine))
                currentLine=[]
                noOfLettersInCurrentLine=0
            currentLine+=[word]
            noOfLettersInCurrentLine+=len(word)
        return result+[' '.join(currentLine).ljust(maxWidth)]
        

            