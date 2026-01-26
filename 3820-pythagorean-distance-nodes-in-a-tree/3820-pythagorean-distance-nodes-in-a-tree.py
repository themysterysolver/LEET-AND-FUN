class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        hash = defaultdict(list)
        adL = defaultdict(list)
        for u,v in edges:
            adL[u].append(v)
            adL[v].append(u)
        def pydist(start):
            q = deque([start])
            dist = 0
            visited = set([start])
            while q:
                l = len(q)
                for _ in range(l):
                    node = q.popleft()
                    hash[node].append(dist)
                    for ad in adL[node]:
                        if ad not in visited:
                            q.append(ad)
                            visited.add(ad)
                dist+=1
        pydist(x)
        pydist(y)
        pydist(z)
        count = 0
        for arr in hash.values():
            arr.sort()
            if arr[0]**2 + arr[1]**2 == arr[2]**2:
                count+=1
        return count
