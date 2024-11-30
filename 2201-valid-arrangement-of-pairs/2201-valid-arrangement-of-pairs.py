class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adL,inD,outD={},{},{}
        for u,v in pairs:
            if u not in adL:
                adL[u]=[]
            adL[u].append(v)
            outD[u]=outD.get(u,0)+1
            inD[v]=inD.get(v,0)+1
        #print(adL,outD,inD)
        for u,v in pairs:
            if v not in adL:
                adL[v]=[]
        result=[]
        start=pairs[0][0]
        for u in outD:
            if outD[u]==inD.get(u,0)+1:
                start=u
                break
        stack=[start]
        while stack:
            node=stack[-1]
            if adL[node]:
                stack.append(adL[node].pop(0))
            else:
                result.append(node)
                stack.pop()
        #print(result)
        result.reverse()
        #print(result)
        pairedResult=[]
        for i in range(1,len(result)):
            pairedResult.append([result[i-1],result[i]])
       #print(pairedResult)
        return pairedResult