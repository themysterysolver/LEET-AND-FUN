class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=dict()
        for i in words:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        print (d)
        a=[[val,key] for key,val in d.items()]
        print (a)
        b=sorted(a,key=lambda x:(-x[0],x[1]))
        print (b)
        c=[b[i][1] for i in range(k)]
        i=0
        return c