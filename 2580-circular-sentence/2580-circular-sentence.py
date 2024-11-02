class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        new=sentence.split()
        #print(new,type(new))
        for i in range(len(new)-1):
            if new[i][-1]==new[i+1][0]:
                pass
            else:
                return False
        return True if new[0][0]==new[-1][-1] else False
