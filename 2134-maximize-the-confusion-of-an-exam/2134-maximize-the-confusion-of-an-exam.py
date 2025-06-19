class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveOne(s,val):
            start=0
            maxi=0
            symbolFlipped=0
            for i in range(len(s)):
                if s[i]==val:
                    symbolFlipped+=1
                while symbolFlipped>k:
                    if s[start]==val:
                        symbolFlipped-=1
                    start+=1
                maxi=max(maxi,i-start+1)
            return maxi
        return max(maxConsecutiveOne(answerKey,"T"),maxConsecutiveOne(answerKey,"F"))