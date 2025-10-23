class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adL = defaultdict(list)
        for idx,val in enumerate(manager):
            adL[val].append(idx)
        q = deque([(informTime[headID],headID)])
        maxi = 0        
        while q:
            c,node = q.popleft()
            maxi = max(c,maxi)
            for nnode in adL[node]:
                q.append((c+informTime[nnode],nnode))
        return maxi


