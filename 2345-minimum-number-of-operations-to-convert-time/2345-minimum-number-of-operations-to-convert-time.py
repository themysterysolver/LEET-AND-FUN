class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        minsCurrent=int(current[3:])+int(current[:2])*60
        minsCorrect=int(correct[3:])+int(correct[:2])*60
        print(minsCurrent,minsCorrect)
        ans=abs(minsCurrent-minsCorrect)
        print(ans)
        count=0
        while ans!=0:
            if ans-60>=0:
                ans-=60
            elif ans-15>=0:
                ans-=15
            elif ans-5>=0:
                ans-=5
            elif ans-1>=0:
                ans-=1
            count+=1
        return count