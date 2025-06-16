class Solution:
    def countHomogenous(self, s: str) -> int:
        def factorial(n):
            return (n*(n+1))//2
        dp=dict()
        dum=""
        count=0
        MOD=10**9+7
        for idx,c in enumerate(s):
            #print(idx,dum,count,dp)
            if idx==0 or dum=='':
                dum=s[idx]
            else:
                if c!=dum[-1]:
                    if len(dum) in dp:
                        count+=dp[len(dum)]
                        count%=MOD
                    else:
                        dp[len(dum)]=factorial(len(dum))
                        #print(idx,"CHECKPOOINT:",dum,len(dum),factorial(len(dum)))
                        count+=dp[len(dum)]
                        count%=MOD
                    dum=c
                else:
                    dum+=c
            #print(idx,dum,count,dp)
        #print(count)
        if len(dum) in dp:
            count+=dp[len(dum)]
            count%=MOD
        else:
            #print("CHECKPOINT-2:",dum,len(dum),factorial(len(dum)))
            count+=factorial(len(dum))
            count%=MOD
        return count