class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adV={i:[i+1] for i in range(n)}
        #print(adV)
        adV[n-1].pop()
        #print(adV)
        result=[]
        def BFS():
            #print('-------------------------------------')
            q=deque([0])
            d=0
            l=len(q)
            visited=[False]*n
            visited[0]=True
            while q:
                #print(d,'q:BEFORE',list(q))
                l=len(q)
                for i in range(l):
                    node=q.popleft()
                    for i in adV[node]:
                        if not visited[i]:
                            q.append(i)
                            visited[i]=True
                d+=1
                #print(d,'q:AFTER',list(q))
                if n-1 in set(list(q)):
                    return d
        for u,v in queries:
            adV[u].append(v)
            result.append(BFS())
        return result
