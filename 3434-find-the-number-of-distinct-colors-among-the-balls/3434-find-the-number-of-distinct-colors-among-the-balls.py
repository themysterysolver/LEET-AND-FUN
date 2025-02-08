class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hash=dict()
        hashC=dict()
        result=[0]*(len(queries))
        for i in range(len(queries)):
            ball,clr=queries[i]
            if ball in hash:
                prevclr=hash[ball]
                hashC[prevclr]-=1
                if hashC[prevclr]==0:
                    del hashC[prevclr]
            hash[ball]=clr
            hashC[clr]=hashC.get(clr,0)+1
            result[i]=(len(hashC))
        return result