class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        badL = defaultdict(list)
        idxx = defaultdict(list)
        for idx,nums in enumerate(routes):
            for num in nums:
                badL[num].append(idx)
            idxx[idx] = nums
        q = deque(badL[source])
        count = 1
        visited = set()
        #print('badL:',badL)
        #print('idxx',idxx)
        if source == target:
            return 0
        while q:
            l = len(q)
            for _ in range(l):
                routes = q.popleft()
                if routes not in visited:
                    #print('routes',routes)
                    for stops in idxx[routes]:
                        #print('stops',stops)
                        if stops == target:
                            return count
                        for i in badL[stops]:
                            if i not in visited:
                                q.append(i)
                    visited.add(routes)
            #print(q)
            count+=1
        return -1
        



        