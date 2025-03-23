class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited=set()
        adL={i:[] for i in range(n)}
        for x,y in edges:
            adL[x].append(y)
            adL[y].append(x)
        #print(adL)
        def BFS(node):
            q=deque([node])
            visit=set()
            visit.add(node)
            node_count=0
            edge_count=0
            while q:
                node_count+=1
                r=q.popleft()
                for nodd in adL[r]:
                    edge_count+=1
                    if nodd not in visit:
                        q.append(nodd)
                        visit.add(nodd)
            visited.update(visit)
            edge_count//=2
            return edge_count==((node_count)*(node_count-1))/2
        for i in range(n):
            if i not in visited:
                if BFS(i):
                    count+=1
        return count
        