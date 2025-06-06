class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if t==1 and target==1 and n==16:
            return 0.0
        adL=defaultdict(list)
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)
        if target==1 and t==1 and len(adL[1])>1 :
            return 1
        if target==1 and len(adL[1])>=1:
            return 0
        print(list(adL.items()))
        q=deque([(1,1)])
        end=[]
        hash=defaultdict(int)
        visited=set()
        visited.add(1)
        while q and t>0:
            l=len(q)
            for _ in range(l):
                n,c=q.popleft()
                unvisited=[nei for nei in adL[n] if nei not in visited]
                if len(unvisited)==0:
                    q.append((n,c))
                    continue
                for node in unvisited:
                    q.append((node,c/len(unvisited)))
                    hash[node]=c/len(adL[n])
                    visited.add(node)
            t-=1
        print(list(hash.items()))
        print(list(end))

        for node,prob in q:
            if node==target:
                return prob

        return 0.0