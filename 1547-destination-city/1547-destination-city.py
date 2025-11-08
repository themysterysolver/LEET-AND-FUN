class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adL = defaultdict(list)
        hash = defaultdict(int)
        p = set()
        for u,v in paths:
            p.add(u)
            p.add(v)
            adL[u].append(v)
            hash[v] += 1
        q = deque([])
        for city in list(p):
            if hash[city] == 0:
                q.append(city)
        last = ""
        while q:
            last = q.popleft()
            for node in adL[last]:
                q.append(node)
        return last
            
        