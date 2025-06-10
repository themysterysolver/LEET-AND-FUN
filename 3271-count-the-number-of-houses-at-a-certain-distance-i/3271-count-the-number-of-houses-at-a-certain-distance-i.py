class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def dist(src,dest):
            q=deque([src])
            visited=set()
            visited.add(src)
            k=1
            while q:
                l=len(q)
                for _ in range(l):
                    n=q.popleft()
                    if n==dest:
                        return k
                    for nei in adL[n]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        visited.add(nei)
                k+=1
        dist_k=[0]*n
        adL=defaultdict(list)
        for i in range(1,n):
            if i!=n:
                adL[i].append(i+1)
                adL[i+1].append(i)
        adL[x].append(y)
        adL[y].append(x)
        #print(adL.items())
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                k=dist(i,j)
                #print(i,j,k)
                dist_k[k-2]+=2
        return dist_k
