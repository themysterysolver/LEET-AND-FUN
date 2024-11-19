class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        #adjaceny list setup,visted+suspicious
        result=[]
        visitedSus=[False]*n
        adL={i:[] for i in range(n)}
        #creating adj list
        print(adL)
        for start,end in invocations:
            adL[start].append(end)
        print(adL)
        #BFS->spread bug(k)
        visitedSus[k]=True
        q=deque([k])
        while q:
            l=len(q)
            for i in range(l):
                node=q.popleft()
                for node in adL[node]:
                    if not visitedSus[node]:
                        visitedSus[node]=True
                        q.append(node)
        print('BUGS FOUND AT:',visitedSus)
        #----END of BFS------
        bigFlag=0
        for key,val in adL.items():
            flag=0
            if not visitedSus[key]:
                for node in val:
                    if visitedSus[node]:
                        print('where?:',key,node,val)
                        flag=1
                        break
            if flag==1:
                bigFlag=1
                break
        print('bigFlag',bigFlag)
        if bigFlag==1:
            print(n)
            return [i for i in range(n)]
        else: 
            return [i for i,val in enumerate(visitedSus) if not val]