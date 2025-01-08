class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1,row2,row3=set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")
        print(row1,row2,row3)
        result=[]
        for word in words:
            w=set(word.lower())
            if w|row1==row1 or w|row2==row2 or w|row3==row3:
                result.append(word)
        return result