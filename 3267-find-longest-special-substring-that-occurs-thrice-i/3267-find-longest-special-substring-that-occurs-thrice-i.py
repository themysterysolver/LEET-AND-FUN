class Solution:
    def maximumLength(self, s: str) -> int:
        hash=dict()
        for i in range(len(s)):
            for j in range(i,len(s)):
                if len(set(s[i:j+1]))==1:
                    hash[s[i:j+1]]=hash.get(s[i:j+1],0)+1
        #print(hash)
        hitems=list(hash.items())
        #print(hitems)
        hitems.sort(key=lambda x:(x[1],len(x[0])),reverse=True)
        print(hitems)
        maxi=0
        for x,y in hitems:
            if len(x)>maxi and y>=3:
                maxi=len(x)
        return maxi if maxi!=0 else -1

        