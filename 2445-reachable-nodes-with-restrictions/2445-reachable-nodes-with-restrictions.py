class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        r = set(restricted)
        adL = defaultdict(list)
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)
        
        visited = set()
        visited.add(0)
        count = 1
        q = deque([0])
        while q:
            node  = q.popleft()
            for nei in adL[node]:
                if nei not in r and nei not in visited:
                    q.append(nei)
                    visited.add(nei)
                    count+=1
        return count