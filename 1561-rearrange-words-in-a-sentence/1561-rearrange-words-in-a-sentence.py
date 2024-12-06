class Solution:
    def arrangeWords(self, text: str) -> str:
        n=text.split(' ')
        t=[(len(n[i]),i,n[i]) for i in range(len(n))]
        print(n,t)
        t.sort(key=lambda x:(x[0],x[1]),reverse=True)
        print(t)
        ans=""
        for a,b,c in t:
            ans=c+" "+ans
        ans=ans.lower()
        ans=ans[0].upper()+ans[1:]
        return ans[:-1]