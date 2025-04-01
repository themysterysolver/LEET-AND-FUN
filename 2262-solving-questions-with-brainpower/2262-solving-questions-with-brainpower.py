class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[0]*len(questions)
        dp[-1],_=questions[-1]
        for i in range(len(questions)-2,-1,-1):
            pt,score=questions[i]
            if i+score+1<len(questions):
                dp[i]=max(dp[i+1],pt+dp[i+score+1])
            else:
                dp[i]=max(pt,dp[i+1])
        return dp[0]